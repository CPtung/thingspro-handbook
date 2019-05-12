import os
import gzip
import json

from influxdb import InfluxDBClient
from flask import Flask
from flask import request
from werkzeug import secure_filename

config = {
    "HOST": os.getenv('DB_HOST', "localhost"),
    "PORT": int(os.getenv('DB_PORT', 8086)),
    "USERNAME": os.getenv('DB_USERNAME', "root"),
    "PASSWORD": os.getenv('DB_PASSWORD', "root"),
    "DATABASE": os.getenv('DB', "thingspro"),
    "SSL": False,
    "SSL_VERIFY": True
}

if os.getenv('DB_SSL', "yes") == "yes":
    config["SSL"] = True

if os.getenv('DB_SSL_VERIFY', "yes") == "yes":
    config["SSL_VERIFY"] = True

print (config)

client = InfluxDBClient(
    host=config["HOST"], port=config["PORT"], username=config["USERNAME"],
    password=config["PASSWORD"], database=config["DATABASE"],
    ssl=config["SSL"], verify_ssl=config["SSL_VERIFY"]
)


def save_to_influxdb(host, rows):
    datas = []
    for row in rows:
        # {
        #     "equ": "My_ioLogik-E2242",
        #     "at": "2015-07-06T14:51:31Z",
        #     "tagList": [
        #         {
        #             "tag": "di0",
        #             "value": 1
        #         },
        #         {
        #             "tag": "ai0",
        #             "value": 3.14,
        #             "unit": "V"
        #         }
        #     ]
        # }
        for tag in row["tagList"]:
            datas.append(
                {
                    "measurement": tag["tag"],
                    "tags": {
                        "host": host,
                        "equipment": row["equ"]
                    },
                    "time": row["at"],
                    "fields": {
                        "value": float(tag["value"]),
                        "unit": tag.get("unit", "N/A")
                    }
                }
            )
    client.write_points(datas)


def save(file):
    filename = secure_filename(file.filename)
    save_path = os.path.join("/tmp", filename)
    file.save(save_path)
    return save_path

app = Flask(__name__)


@app.route("/file/<host>", methods=["POST"])
def post_gz(host):
    file = request.files['file']
    if ".json.gz" in file.filename:
        with gzip.open(save(file), "r") as f:
            objs = json.load(f)
    elif ".json" in file.filename:
        with open(save(file), "r") as f:
            objs = json.load(f)
    else:
        return "Test OK"

    save_to_influxdb(host, objs)
    return "Uploaded. compressed file."


@app.route("/json/<host>", methods=["POST"])
def post_json(host):
    save_to_influxdb(host, request.get_json())
    return "Posted."


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

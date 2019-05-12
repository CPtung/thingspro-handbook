# Develop Your Bundle

Refer to bundle-programming chapter. Here we download the example bundle and a new Sanji bundle will be decompressed in the home directory.
```sh
moxa@moxa:~$ tree .
.
└─ sanji-bundle-example
    ├── bundle.json              # metadata about this bundle
    ├── data
    │   └── example.json.factory # persistent config data (in JSON format)
    ├── index.py                 # bundle entry point (resources handler)
    ├── README.md
    └── requirements.txt         # python requirements file
2 directories, 5 files
```

## Develop Your Bundle on PC

Now, you can start develop the methods for handling the requests from web. Change directory to the folder you created in above steps. Edit the persistent config data `/data/example.json.factory` to define the parameters you need.

**Example:**

Define `UserName` for the bundle:
```json
{
    "UserName": "Admin"
}
```

## Edit index.py

There are two HTTP methods \(GET, PUT\) in index.py. Based on your need, you can develop your code to handle requests in those code areas.

- For HTTP [GET] method (Resource URI: /example)

```python
    @Route(methods="get", resource="/example")
    def _get(self, message, response):

        # insert your code here to handle the requests
        # You may execute system command or your own programs

        return response(data=self.model.db)
```

- For HTTP [PUT] method (Resource URI: /example)

```python
    @Route(methods="put", resource="/example")
    def _put(self, message, response):
        try:
            self.model.db = message.data
            self.model.save_db()

            # insert your code here to handle the requests
            # You may execute system command or your own programs

        except Exception as e:
            return response(code=400, data={"message": e.message})
        return response(data=message.data)
```

After finishing your code, remember to save it.

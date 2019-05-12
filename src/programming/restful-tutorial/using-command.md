# Using the CURL Command

This section demonstrates the use of the `curl` command to interact with a *RESTful API* to request resources. The API response is in JSON format.

The `curl` utility is a command-line tool available on Unix, Linux, Mac OS, X Windows, and many other platforms. This utility provides easy direct access to the HTTP protocol from the command-line and is therefore an ideal way to interact with ThingsPro via the HTTP RESTful API.

## Using `mx-api-token`

> Refer to [Get API Token](get-api-token.md) for details on acquiring a `mx-api-token`

Usage: Include the `mx-api-token` token in the header and specify the `--insecure` option to skip certificate validation. For simple `GET` requests use the following:
```
$ curl --insecure -H 'mx-api-token: <token>' \
       [-X GET] https://localhost/api/v1/<resource>
```

For `PUT`, `POST` or `DELETE` request for JSON data, use the following:
```
$ curl --insecure -H 'mx-api-token: <token>' \
       -H 'Content-Type: application/json' \
       -X <POST|PUT|DELETE> https://localhost/api/v1/<resource> \
       -d '<DATA>'
```

## Getting a Resource

Usage: For simple `GET` requests, just provide the URL of the request in the `-X GET` command. The `-X GET` command specifies the `GET` option, which is the default operation of the `curl` command.
```
$ curl --insecure -H 'mx-api-token: <token>' \
       [-X GET] https://localhost/api/v1/<resource>
```

### Example of a GET Request

The following example requests the first port mapping rule:
```
$ curl --insecure -H 'mx-api-token: <token>' \
       https://localhost/api/v1/network/portmapping/1
```

The response from the port mapping resource in JSON format is given below:
```json
{
  "id": 1,
  "enable": true,
  "service": "http",
  "portStart": 80,
  "portEnd": 80,
  "destIp": "192.168.5.123",
  "protocol": "tcp"
}
```

Some resources provide a *collection* of content as in the following case:

```
$ curl --insecure -H 'mx-api-token: <token>' \
       https://localhost/api/v1/network/portmapping
```

```json
[
  {
    "id": 1,
    "enable": true,
    "service": "http",
    "portStart": 80,
    "portEnd": 80,
    "destIp": "192.168.5.123",
    "protocol": "tcp"
  },
  {
    "id": 2,
    "enable": false,
    "service": "test",
    "portStart": 12340,
    "portEnd": 12345,
    "destIp": "192.168.5.123",
    "protocol": "both"
  }
]
```

## Creating/Updating a Resource

Usage: Specify a header using the `-H` option and provide data using the `-d` option.
```
$ curl --insecure -H 'mx-api-token: <token>' \
       -H 'Content-Type: application/json' \
       -X <POST|PUT> https://localhost/api/v1/<resource> \
       -d '<DATA>'
```

### Example of a POST Request 

The following command creates a port mapping rule using the `curl` command:
```
$ curl --insecure -H 'mx-api-token: <token>' \
       -H 'Content-Type: application/json' \
       -X POST https://localhost/api/v1/network/portmapping \
       -d '{ "enable": true,
             "service": "http",
             "portStart": 8080,
             "portEnd": 8080,
             "destIp": "192.168.5.123",
             "protocol": "tcp"}'
```

After the create (*POST*) command is processed, an `id` is assigned and included in the JSON response.
```json
{
  "id": 2,
  "enable": true,
  "service": "http",
  "portStart": 8080,
  "portEnd": 8080,
  "destIp": "192.168.5.123",
  "protocol": "tcp"
}
```

### Example of a PUT Request

The following command requests an update to the second port mapping rule:
```
$ curl --insecure -H 'mx-api-token: <token>' \
       -H 'Content-Type: application/json' \
       -X PUT https://localhost/api/v1/network/portmapping/2 \
       -d '{ "id": 2,
             "enable": true,
             "service": "http",
             "portStart": 8000,
             "portEnd": 8000,
             "destIp": "192.168.5.123",
             "protocol": "tcp"}'
```

The response to the PUT request is as shown below:
```json
{
  "id": 2,
  "enable": true,
  "service": "http",
  "portStart": 8000,
  "portEnd": 8000,
  "destIp": "192.168.5.123",
  "protocol": "tcp"
}
```

## Deleting a Resource
Usage: Specify the URL of the resource that you want to delete.
```
$ curl --insecure -H 'mx-api-token: <token>' \
       -X DELETE https://localhost/api/v1/<resource>
```

### Example of a DELETE Request

To delete a port mapping rule with `id = 2`, use the following command:
```
$ curl --insecure -H 'mx-api-token: <token>' \
       -X DELETE https://localhost/api/v1/network/portmapping/2
```

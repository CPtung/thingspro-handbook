# Using RESTful API Calls in Python Programs

Developers can use the the `requests` library to call *RESTful API* in *Python* programs.

## `Requests Library`
> The *Requests* library is an easy-to-use HTTP library in Python.  
> For additional details on Python Requests library, visit:
> http://docs.python-requests.org/

### Installing the Requests Library

Log on to ThingsPro Gateway via a console port or an Ethernet SSH daemon and type 
the following command to install the Python Requests library: 

```pip install requests```

### Getting a Resource

To get the current system status, do the following:

1. Create a file `get_system_status.py` with *execution* permission.
2. Include the following code in the file:

```py
#!/usr/bin/env python

import requests

headers = {
    "mx-api-token": "<token>"
}

r = requests.get(
        'https://localhost/api/v1/system/status',
        headers=headers,
        verify=False)
data = r.json()

print (data)
```
Note: The response to the request is assigned to `data`.

### Updating a Resource with JSON Payload

To update a resource with JSON payload, do the following:

1. Enable fixed DNS and set the primary DNS to a`8.8.8.8` and secondary DNS to `168.96.1.1`.
2. Create a file `set_dns.py` with *execution* permission and include the following code in the file:

```py
#!/usr/bin/env python

import requests

headers = {
    "mx-api-token": "<token>",
    "Content-Type": "application/json"
}

dns = {
    "enableFixed": True,
    "fixedDns": ["8.8.8.8", "168.95.1.1"]
}

r = requests.put(
        'https://localhost/api/v1/network/dns',
        headers=headers,
        json=dns,
        verify=False
    )

resp_data = r.json()

print (resp_data)
```

> For details on acquiring a `mx-api-token`, refer to [Get API Token](get-api-token.md). 
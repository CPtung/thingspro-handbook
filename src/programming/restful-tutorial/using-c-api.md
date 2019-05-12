# Using the ThingsPro API in C Programs

Developers who want to integrate the ThingsPro *Configuration API* with their *C* programs can use the `libcurl` library. The `libcurl` library is an easy-to-use free client-side URL transfer library, which can be used to build applications for various platforms.

## `libcurl`
The libcurl library provides interfaces that you can use to start a libcurl easy session, set the interface options, and send requests based on the options selected. If you do not want to reuse a session after you receive a response, you must close the session.

## Using `libcurl`
The `libcurl` library provides the `curl-config` tool that you can use to find the library path and the required flags.

Including `curl.h` in your source code:
```c
#include <curl/curl.h>
```

Compiling your source code:
```
$ gcc -c example.c -o example.o `curl-config --cflags`
```

Linking your code:
```
$ gcc -o example example.o `curl-config --libs`
```

### Initialization and Cleanup

The `libcurl` library should be initialized as follows to get the easy-session handle before you can use the library:
```c
CURL *curl = curl_easy_init();
```

Use the following command to clean up the easy-session handle after all operations are complete:
```c
/* always cleanup */
curl_easy_cleanup(curl);
```

### Setting Basic Options

Set a resource for `CURLOPT_URL` as follows:
```c
/* Apply mx-api-token */
struct curl_slist *headers = NULL;
headers = curl_slist_append(headers, "mx-api-token: <token>");

/* Set URL */
curl_easy_setopt(curl, CURLOPT_URL, "https://localhost/api/v1/<resource>");

/* Skip verification of the server certificate. */
curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);

/* Skip verificaton of the certificate name against the host. */
curl_easy_setopt(curl, CURLOPT_SSL_VERIFYHOST, 0L);
```
Note: To access ThingsPro via HTTPS, you must disable `CURLOPT_SSL_VERIFYPEER` and `CURLOPT_SSL_VERIFYHOST`.

> Refer to [Get API Token](get-api-token.md) for details on acquiring the `mx-api-token`.

### Performing the Request

```c
/* Perform the request, res will get the return code */
res = curl_easy_perform(curl);
```
After the request is performed, the status is assigned to `res`. If `CURLOPT_WRITEFUNCTION` is not set, the response will be printed to `stdout` by default. For a list of libcurl error codes, visit: https://curl.haxx.se/libcurl/c/libcurl-errors.html 

## Getting the Resource(s)

To get a resource, assign a URL to `CURLOPT_URL` and then perform the request.

## Creating a Resource

To `POST` data, define the header as follows:
```c
headers = curl_slist_append(headers, "Content-Type: application/json");
```

Specify the data for the `POST` request using the following string format:
```c
curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json_str);
```

## Updating a Resource

To `PUT` data, define the header as follows:
```c
headers = curl_slist_append(headers, "Content-Type: application/json");
```

Specify the data for the `PUT` request using the string format:
```c
curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "PUT");
curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json_str);
```

Specify the information of the file to include:
```c
#include <fcntl.h>
#include <sys/stat.h>

FILE *fd;
struct stat file_info;

stat(file, &file_info);
fd = fopen(file, "rb");
```

Using a file for the `PUT` data request:

```c
/* enable uploading */
curl_easy_setopt(curl, CURLOPT_POSTFIELDS, json_str);

/* specify which file to upload */
curl_easy_setopt(curl, CURLOPT_READDATA, fd);

/* provide the size of the upload. We specifically typecast the value
   to curl_off_t since we must be sure to use the correct data size */
curl_easy_setopt(curl, CURLOPT_INFILESIZE_LARGE,
                 (curl_off_t)file_info.st_size);
```

## Deleting a Resource

Using `CURLOPT_CUSTOMREQUEST` to specify a `DELETE` request:
```c
curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "DELETE");
```

## Examples

Download the examples available in the [libcurl-example.tar.gz](./libcurl-example.tar.gz) file. These examples are for demonstration purposes only and contain the following programs:

| Code | Description |
|:---- |:----------- |
| [https_get.c](libcurl-example/https_get.c) | Simple HTTPS GET |
| [https_get_write_cb.c](libcurl-example/https_get_write_cb.c) | Shows how the write callback function can be used after GET |
| [https_post.c](libcurl-example/https_post.c) | Simple HTTPS POST |
| [https_put.c](libcurl-example/https_put.c) | Simple HTTPS PUT |
| [https_put_by_file.c](libcurl-example/https_put_by_file.c) | HTTP PUT with easy interface from a file |
| [https_put_read_cb.c](libcurl-example/https_put_read_cb.c) | HTTP PUT with easy interface from a file and read callback |
| [https_delete.c](libcurl-example/https_delete.c) | Simple HTTPS DELETE ||

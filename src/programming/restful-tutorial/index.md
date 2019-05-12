# RESTful API Tutorials

## Overview

ThingsPro Gateways (e.g., UC-8112-LX) provide a *RESTful API* programming interface for developers who want to interact with the ThingsPro platform and integrate their software with the platform. Excluding web account operations, you can use the ThingsPro RESTful API for all other gateway functions such as *bootstrap*, *ethernet*, and *iptables*.

This document gives you an overview of how to use the ThingsPro *RESTful API* in your program and includes information such as the resources available, HTTPS methods supported, and format of the requests and responses.


### Constraints in ThingsPro v2.0

1. The ThingsPro RESTful API can only be accessed with a valid access token.
2. We do not recommend the simultaneous use of the ThingsPro RESTful API and the ThingsPro web interface.


## Introduction

The ThingsPro API provides access to a number of resources that can be accessed via HTTPS requests. The response format is JSON. Because REST is based on web technologies, you do not need external libraries to use RESTful APIs. You can start interacting with the ThingsPro API using your web browser.

## URI Structure

The format of the REST URI is as follows:

```
https://localhost/api/v1/<resource>
```

The final part of the URI is the name of the resource, which determines the response that you will receive from the API. Some resources may require additional path parameters to identify a specific resource. For example, the URI to access the first Ethernet interface is given below:

```
https://localhost/api/v1/network/ethernets/1
```

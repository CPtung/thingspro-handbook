# Using the C API

The C API libraries come with C-header files and shared objects. 
The `libmxidaf` API provides *pkg-config* support to compile your source code, which you can use as follows:

```
$ gcc -c example.c -o example.o `pkg-config --cflags`
```

To link your code, use the following command:

```
$ gcc -o example example.o `pkg-config --libs`
```

## Initializing the Tag Library

To initialize the tag library, create a `tag` instance.

To create a `tag` instance in C, use the following command:
```c
tag *tag_inst = tag_new();
```

## Deleting a Tag Instance

To delete a Tag instance in C, use the following command:
```c
tag_delete(tag_inst);
```

## Publishing Tags

To publish tags, use `tag_publish()`.

```c
value_t value_data;
value_data.d = 1.38;

int rc = tag_publish(
    tag_inst,
    "Equipment-Name",
    "Tag-Name",
    value_data,
    TAG_VALUE_TYPE_DOUBLE,
    "",
    "2016-09-20T11:11:40Z");
```

### Sample

A sample application is available at:

  `/usr/share/mxdaf/libmxidaf/sample/publish.c`

## Subscribing to Tags

To subscribe to Tags, use `tag_subscribe()` or `tag_subscribe_callback()` as follows:

```c
tag_subscribe(
    tag_inst,
    "Subscribe_Equipment",
    "SubScribe_Tag");
```

```c
void my_callback_func(
    tag *tag_inst,
    const char *equipment_name,
    const char *tag_name,
    value_t *value,
    value_type_t value_type,
    const char *unit,
    const char *timestamp)
{
}

tag_subscribe_callback(
    tag_inst,
    my_callback_func);
```

### Sample

A sample application is available at:

  `/usr/share/mxdaf/libmxidaf/sample/subscribe.c`

## Initializing the Modbus Library

To initialize the modbus library, create a `mxmodbus` instance.

To create a `mxmodbus` instance in C, use the following command:
```c
mxmodbus *mxmodbus_inst = mxmodbus_new();
```

## Deleting a Modbus Library Instance

To delete a `mxmodbus` instance in C, use the following command:
```c
mxmodbus_delete(mxmodbus_inst);
```

## Reading Modbus Tags

To read Modbus Tags, use `mxmodbus_read()`.

```c
#define MODBUS_READ_TIMEOUT_MS 1000

value_t value_data;
value_type_t value_type;

int rc = mxmodbus_read(
    mxmodbus_inst,
    "Equipment-Name",
    "Tag-Name",
    MODBUS_READ_TIMEOUT_MS,
    &value_data,
    &value_type
);
```

### Sample

A sample application is available at:

  `/usr/share/mxdaf/libmxidaf/sample/modbus.c`

## Writing Values into Modbus Tags

To write values into Modbus Tags, use `mxmodbus_write()`.

```c
#define MODBUS_WRITE_TIMEOUT_MS 1000

value_t value_data;
value_data.d = 1.38

int rc = mxmodbus_write(
    mxmodbus_inst,
    "Equipment-Name",
    "Tag-Name",
    MODBUS_WRITE_TIMEOUT_MS,
    value_data,
    TAG_VALUE_TYPE_DOUBLE
); 
```

### Sample

A sample application is available at:

  `/usr/share/mxdaf/libmxidaf/sample/modbus.c`

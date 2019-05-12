# Using the Python API

The Python *libmxidaf* library comes pre-installed in the ThingsPro Gateway. To use the library, just import it in your Python source file.

```py
from libmxidaf_py import TagV2, Modbus
```

## Initializing the Tag Library

To initialize the library, get an instance of `TagV2`.

To get `TagV2` instance in Python, do the following:

```py
tagv2 = TagV2.instance()
```

## Publishing Tags

To publish Tags, use `TagV2.publish()`.

```py
from libmxidaf_py import Tag, Time, Value

tagv2.publish(
    "Equipment-name",
    "Tag-Name",
    Tag(
        Value(1.38),
        Time.now(),
        "Unit"
    )
)
```

### Sample

A sample application is available at:

  `/usr/share/mxdaf/libmxidaf_py/sample/publish.py`

## Subscribing to Tags

To subcribe to Tags, use `TagV2.subscribe() or TagV2.subscribe_callback()` as follows:

```py
tagv2.subscribe(
    "Subscribe_Equipment",
    "SubScribe_Tag");
```

```py
def my_callback_func(equipment_name, tag_name, tag):
    # do something here
    pass

tagv2.subscribe_callback(my_callback_func)
```

### Sample

A sample application is available at:

  `/usr/share/mxdaf/libmxidaf_py/sample/subscribe.py`

## Initializing the Modbus Library

To initialize the modbus library, create a `Modbus` instance.

To create `Modbus` instance in Python, do the following:
```py
modbus = Modbus.instance();
```

## Reading the Modbus Tags

To read Modbus Tags, use `Modbus.read()`.

```py
tag = modbus.read("Equipment-Name", "Tag-Name")
```

### Sample

A sample application is available at:

  `/usr/share/mxdaf/libmxidaf_py/sample/modbus.py`

## Updating Modbus Tags

To write values to Modbus Tags, use `Modbus.write()`.

```py
from libmxidaf_py import Tag, Time, Value

modbus.write(
    "Equipment-Name",
    "Tag-Name",
    Tag(
        Value(1.38),
        Time.now(),
        "Unit"
    )
)
```

### Sample

A sample application is available at:

  `/usr/share/mxdaf/libmxidaf_py/sample/modbus.py`

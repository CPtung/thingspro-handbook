## In/Out Interfaces

### Man Page
```
NAME
    mxtagimport

SYNOPSIS
    mxtagimport [--mqtt-broker-host HOST] [--mqtt-broker-port PORT] [IMPORT_OPTIONS...]

DESCRIPTION
    --mqtt-broker-host HOST
    --mqtt-broker-port PORT
        Use HOST and PORT to connect to MQTT broker to subscribe readings.

        Default HOST and PORT are "127.0.0.1" and 1883.

IMPORT OPTIONS
    --equipment EQUIPMENT
        Equipment name.

        Must be given.

    --tag TAG
        Tag name.

        Must be given.

    --type TYPE
        Assign value type.

        If this option is not given, mxtagimport would try to parse VALUE and
        choose a proper value type itself.

        Allowed TYPE:
            int
            uint
            float
            string

    --value VALUE
        Tag value.

        Must be given.

    --at TIME
        Given timestamp.

        If this option is not given, mxtagimport uses system time as timestamp.

        Format:
            YYYY-mm-ddTHH:MM:SS[.ffffff]Z

        Example:
            2016-02-17T09:59:12Z
            2016-02-17T09:59:12.123456Z

    --unit UNIT
        Given unit.

        Default "".

EXIT STATUS
    0
        Success.
    1
        Unknown error.
    2
        Illegal argument.
    3
        I/O error.
    4
        Import error.
```

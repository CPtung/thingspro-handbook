## In/Out Interfaces

### Man Page
```
NAME
    mxtaghistory

SYNOPSIS
    mxtaghistory [-f MXHTAG] [QUERY_OPTIONS...]

DESCRIPTION
    -f MXHTAG
        Given the path to mxhtag database file.

        Default '/dev/shm/mxhtag.sqlite3'.

QUERY OPTIONS
    --last COUNT
        Dump last COUNT values of each Tag collected by Data Acquisition Framework.

        Example:
        $ mxtaghistory --last 1
        "equipment","tag","at","value","unit"
        "My_ioLogik-E2242","di0","2015-07-06T14:51:31Z","1",
        "My_ioLogik-E2242","ai0","2015-07-06T14:51:31Z","3.14","V"
        "My_other_ioLogik-E2242","DOOR_STATUS","2015-08-19T15:09:24Z","1",
        "My_other_ioLogik-E2242","WINDOW_STATUS","2015-08-19T15:09:24Z","0",

    --equipment EQUIPMENT
        Equipment name.

        Dumps all Tags belong to EQUIPMENT.

        Example:
        $ mxtaghistory --latest 1 --equipment My_ioLogik-E2242
        "equipment","tag","at","value","unit"
        "My_ioLogik-E2242","di0","2015-07-06T14:51:31Z","1",
        "My_ioLogik-E2242","ai0","2015-07-06T14:51:31Z","3.14","V"

    --tag TAG
        Tag name.

        Can only be used when --equipment is given.

        When given, mxtaghistory dumps Tags that matches TAG.

        Can be given multiple times.

        Example:
        $ mxtaghistory --latest 1 --equipment My_ioLogik-E2242 --tag di0
        "equipment","tag","at","value","unit"
        "My_ioLogik-E2242","di0","2015-07-06T14:51:31Z","1",

EXIT STATUS
    0
        Success.
    1
        Unknown error.
    2
        Illegal argument.
    3
        DB access failure.
    4
        Internal error.
```

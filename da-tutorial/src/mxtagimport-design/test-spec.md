## Test Spec

### Import Behavior

Verify that `mxtagimport` imports Tags correctly.

After each step, query for the value imported to verify its correctness:
    ```
    $ mxtaghistory --last 1
    ```

1. Import float.
    ```
    $ mxtagimport --equipment test-eq --tag float-tag --value 3.14
    ```

2. Import string.
    ```
    $ mxtagimport --equipment test-eq --tag string-tag --value hohoho
    ```

3. Import with timestamp.
    ```
    $ mxtagimport --equipment test-eq --tag float-tag --value 3.14 --at 2016-04-08T11:44:17Z
    ```

4. Import with unit.
    ```
    $ mxtagimport --equipment test-eq --tag float-tag --value 3.15 --unit blah
    ```

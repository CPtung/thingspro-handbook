## Test Spec

### Comand Line Interface

Call `import` from C-sample a few times to generate test data.

Use underlying command line to verify `mxtaghistory` command line interface behavior.

1. Dump all.
    ```
    $ mxtaghistory
    ```

2. Query last 3.
    ```
    $ mxtaghistory --last 3
    ```

3. Query by specific equipment.
    ```
    $ mxtaghistory --equipment electrical-probe
    ```

4. Query by specific tag.
    ```
    $ mxtaghistory --equipment electrical-probe --tag voltage
    ```

5. Query last 1 tag by specific tag.
    ```
    $ mxtaghistory --equipment electrical-probe --tag voltage --last 1
    ```

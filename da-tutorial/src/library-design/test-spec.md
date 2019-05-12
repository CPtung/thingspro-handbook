## Test Spec

### Sample Correctness

Verify that the sample sources provided run correctly.

#### C
1. Compile.
    ```
    $ make -C /usr/share/mxdaf/libmxidaf/sample
    ```

2. Run.
    ```
    $ /usr/share/mxdaf/libmxidaf/sample/import
    $ /usr/share/mxdaf/libmxidaf/sample/query
    $ /usr/share/mxdaf/libmxidaf/sample/calculate
    ```

#### Python
1. Run.
    ```
    $ python /usr/share/mxdaf/libmxidaf_py/sample/import.py
    $ python /usr/share/mxdaf/libmxidaf_py/sample/query.py
    $ python /usr/share/mxdaf/libmxidaf_py/sample/calculate.py
    ```

### Robustness Test

Continuously query and import Tags.
Shall not crash.
Memory usage should be stable.

#### C
1. Compile `$(MXDAF)/libmxidaf/tests/robustness.c` on CG.

    ```
    $ gcc -o robustness `pkg-config --libs libmxidaf` robustness.c
    ```

2. Run `robustness`.

    ```
    $ ./robustness
    ```

3. Monitor memory usage of `robustness`, it should be stable for at least 24 hours.

#### Python
1. Run `$(MXDAF)/libmxidaf_py/tests/robustness.py` on CG.
    ```
    $ python robustness.py
    ```

2. Monitor memory usage of `robustness.py`, it should be stable for at least 24 hours.

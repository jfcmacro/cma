# (C)ontinuous (M)emory (A)lgorithms (cma)

This is is a simulator of continuous memory algorithms:

   * first fit
   * best fit
   * worst fit

Each algorithm receives three parameters:
   * `mem_avail`: a list of tuples, base and limit.
   * `req`: a size request for memory.
   * `index` position on the `mem_avail`. This is a circular index: `(index % len(mem_avail))`.

Each algorithm returns two possible values: `None` if the
request cannot be fulfilled, or a quadruple:
   * `mem_avail`: a list of tuples of memory that are newly available (could be empty).
   * `base`: new base where the requested process start.
   * `limit`: new limit.
   * `index`: an index on the `mem_avail` where the request was found. If the
     memory were exhausted, the next valid position would be available.

## Test

First, set the `PYTHONPATH` variable replace (`<path-of-your-project`)
with your directory path.

Linux

```shell
export PYTHONPATH=$PYTHONPATH:<path-of-your-project>
```

Install two libraries

```shell
python3 -m pip install pytest parameterized
```

```shell
python -m pip install pytest parameterized
```

Windows

```shell
SET PYTHONPATH=%PYTHONPATH%;<path-of-your-project>
```

Install two libraries

```shell
python3 -m pip install pytest parameterized
```

```shell
python -m pip install pytest parameterized
```


Running the test, replace with the name of your algorithm implementation: `first`, `best`, `worst`.

```shell
python3 -m unittest test/test_basic_<your_algorithm>_fit.py
python3 -m unittest test/test_other_<your_algorithm>_fit.py
```

```shell
python -m unittest test/test_basic_<your_algorithm>_fit.py
python -m unittest test/test_other_<your_algorithm>_fit.py
```

## Execute cma simulator

First install click

```shell
python3 -m pip install click
```

```shell
python -p pip install click
```

To run the program

```shell
python3 cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt
```

```shell
python cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt
```

The previous execution executes all algorithms you can change to execute different algorithm.

### To execute the first algorithm.

```shell
python3 cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt --function first
```

```shell
python cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt --function first
```

### To execute the best algorithm.

```shell
python3 cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt --function best
```

```shell
python cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt --function best
```

### To execute the worst algorithm.

```shell
python3 cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt --function worst
```

```shell
python cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt --function worst
```

### To execute in different possition

```shell
python3 cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt --pos 3
```

```shell
python cma.py --memmap .\resources\memmap\memmap_1.txt --reqs .\resources\reqs\req_1.txt --pos 3
```





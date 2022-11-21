# mathfn

This is a library with very fast implementations of numerical math functions.

## Example in CPython

To run an example in regular CPython, install LPython so that `lpython` is in
your `$PATH`, then:

```console
$ PYTHONPATH=".:$(lpython --get-rtlib-header-dir)/../ltypes" python examples/example_sin.py
1.5
```

## Example in LPython

To run an example in LPython, install LPython so that `lpython` is in
your `$PATH`, then:

```console
$ lpython examples/example_sin.py
1.50000000000000000e+00
```

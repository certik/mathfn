# mathfn

This is a library with very fast implementations of numerical math functions.

PyPI: https://pypi.org/project/mathfn/

## Example in CPython

To run an example in regular CPython, install LPython so that `lpython` is in
your `$PATH`, then:

```console
$ PYTHONPATH="src:$(lpython --get-rtlib-header-dir)/../ltypes" python examples/example_sin.py
1.5
```

## Example in LPython

To run an example in LPython, install LPython so that `lpython` is in
your `$PATH`, then:

```console
$ lpython -I src examples/example_sin.py
1.50000000000000000e+00
```

## Upload to PyPI

```
python setup.py sdist
pip install twine
twine upload dist/*
```

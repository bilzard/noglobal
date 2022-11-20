# noglobal

This python package provides the `@noglobal` decorator which prohibits the use of global variables from the function scope.

## Install

```bash
pip install noglobal
```

## Usage

```python
from noglobal import NoGlobal
noglobal = NoGlobal(globals()).noglobal

bar = 10
@noglobal
def foo():
    print(bar)
foo()
```
```
NameError                                 Traceback (most recent call last)
Input In [4], in <cell line: 5>()
      2 @noglobal
      3 def foo():
      4     print(bar)
----> 5 foo()

Input In [4], in foo()
      2 @noglobal
      3 def foo():
----> 4     print(bar)

NameError: name 'bar' is not defined
```

## FAQ

### How all this works?

The function with `@noglobal` decorator are re-created as a `type.FunctionType` object, with no global variables.

### All globals are affected?

No. Althogh this package name is "noglobal", the globals below are not affected:
1. modules
2. callable objects (which means the objects which have `__call__` method)

Thus you can not bother importing already imported modules everytime, and so on for the funcsions or classes.

### Can we use explicit global variables?

No. Functions with the `@noglobal` decorator also disallow the explicit use of global variables. That is, if you update a variable bound by a `global` declaration within a function, the original global variable will not be affected.
The following code prints `10` on the standard output.

```python
bar = 10

@noglobal
def foo():
    global bar
    bar = 11
foo()
print(bar)
```

### What happens for the nested functions?

Nested functions in the function decorated with `@noglobal` are also affected.
For example, the code below returns error:

```python
buzz = 11

@noglobal
def foo():
    def bar():
        print(buzz)
    bar()

foo()
```

```
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In [8], line 1
----> 1 foo()

Cell In [7], line 5, in foo()
      3 def bar():
      4     print(buzz)
----> 5 bar()

Cell In [7], line 4, in foo.<locals>.bar()
      3 def bar():
----> 4     print(buzz)

NameError: name 'buzz' is not defined
```

## Attribution

Based on the source codes:
- originally posted in StackOverflow: (CC BY-SA 3.0)
  - skyking: https://stackoverflow.com/questions/31023060/disable-global-variable-lookup-in-python/31047259#31047259
  - Glenn Maynard: https://stackoverflow.com/questions/4858100/how-to-list-imported-modules/4858123#4858123
- later modified by
  - Axel Huebl: https://gist.github.com/ax3l/59d92c6e1edefcef85ac2540eb056da3
  - yoshipon: https://gist.github.com/yoshipon/3adba8cc5d7daac6c3256c9163f48920
  - raven38: https://gist.github.com/raven38/4e4c3c7a179283c441f575d6e375510c

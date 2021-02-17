import pytest, sys, pathlib
if not str(pathlib.Path.cwd()) in sys.path:
    sys.path.append(str(pathlib.Path.cwd()))
from sampleproject.MySampleProgram.PythonProgram import my_decorators

def test_my_decorator_func_s_r_e():
    pass


def test_my_wrap():
    pass



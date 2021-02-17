import pytest, sys, pathlib
if not str(pathlib.Path.cwd()) in sys.path:
    sys.path.append(str(pathlib.Path.cwd()))
from sampleproject.MySampleProgram.PythonProgram import Wraps

def test_my_decorator():
    pass


def test_wrap():
    pass



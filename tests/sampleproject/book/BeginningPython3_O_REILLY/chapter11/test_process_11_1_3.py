import pytest, sys, pathlib
if not str(pathlib.Path.cwd()) in sys.path:
    sys.path.append(str(pathlib.Path.cwd()))
from sampleproject.book.BeginningPython3_O_REILLY.chapter11 import process_11_1_3

def test_washer():
    pass


def test_dryer():
    pass



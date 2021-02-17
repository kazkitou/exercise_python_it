import pytest, sys, pathlib
if not str(pathlib.Path.cwd()) in sys.path:
    sys.path.append(str(pathlib.Path.cwd()))
from sampleproject.book.BeginningPython3_O_REILLY.chapter10 import process_10_3_2

def test_do_this():
    pass


def test_whoami():
    pass



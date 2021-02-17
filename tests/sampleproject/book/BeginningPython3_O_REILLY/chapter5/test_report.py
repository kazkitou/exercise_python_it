import pytest, sys, pathlib
if not str(pathlib.Path.cwd()) in sys.path:
    sys.path.append(str(pathlib.Path.cwd()))
from sampleproject.book.BeginningPython3_O_REILLY.chapter5 import report

def test_get_description():
    pass



import pytest, sys, pathlib
if not str(pathlib.Path.cwd()) in sys.path:
    sys.path.append(str(pathlib.Path.cwd()))
from sampleproject.book.BeginningPython3_O_REILLY.chapter5.boxes.sources import daily

def test_forecast():
    pass



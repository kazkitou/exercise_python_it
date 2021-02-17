import pytest, sys, pathlib
if not str(pathlib.Path.cwd()) in sys.path:
    sys.path.append(str(pathlib.Path.cwd()))
from sampleproject.MySampleProgram.PythonProgram import ctrl_json_file

def test_read_json_file_data():
    pass



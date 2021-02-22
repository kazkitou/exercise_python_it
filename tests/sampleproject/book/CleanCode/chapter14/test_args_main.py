import pytest, sys, pathlib

if not str(pathlib.Path.cwd()) in sys.path:
    sys.path.append(str(pathlib.Path.cwd()))
from sampleproject.book.CleanCode.chapter14 import args_main


def test_args_main():
    pass


if __name__ == "__main__":
    pass

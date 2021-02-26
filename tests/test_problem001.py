import pytest, sys, pathlib

sys.path.append(str(pathlib.Path.cwd()))

from sampleproject.www.Project_Euler.problem001_050 import problem001


def test_problem001():
    assert problem001.problem_1() == 233168

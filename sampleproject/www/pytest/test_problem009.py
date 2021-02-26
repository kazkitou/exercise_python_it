import pytest, sys, pathlib

sys.path.append(
    str(pathlib.Path("C:\\Users\\jas-kaito\\Documents\\my_git\\exercise_python_it"))
)

from sampleproject.www.Project_Euler.problem001_050 import problem009


def test_func1():
    assert problem009.problem_9() == 31875000


def test_func2():
    assert problem009.judge_pythagorean(3, 4, 5) == True


def test_func3():
    assert problem009.judge_pythagorean(200, 375, 425) == True


def test_func4():
    assert problem009.judge_pythagorean(200, 374, 426) == False


def test_func5():
    assert problem009.calc_product([3, 4, 5, 0]) == 0


def test_func6():
    assert problem009.calc_product([3, 4, 5]) == 60


def test_func7():
    assert problem009.calc_product([200, 375, 425]) == 31875000

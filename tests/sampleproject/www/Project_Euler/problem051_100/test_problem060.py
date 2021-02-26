import pytest
from sampleproject.www.Project_Euler.problem051_100 import problem060


def test_resolved_problem():
    cls = problem060.problem_060()
    cls.prim_set = [3, 7, 109, 673]
    assert cls.resolved_problem() == 792


test_is_prim_decision_list = [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
    (11, True)
]
@pytest.mark.parametrize("num, exp", test_is_prim_decision_list)
def test_is_prim_decision(num, exp) -> None:
    cls = problem060.problem_060()
    assert cls.is_prim_decision(num) == exp


test_is_quite_remarkable_prim_number_combination_list = [
    ((3, 7, 109, 673), True),
    ((4, 7, 109, 673), False),
    ((2, 3, 5, 7), False)
]
@pytest.mark.parametrize("prim_num_list, exp", test_is_quite_remarkable_prim_number_combination_list)
def test_is_quite_remarkable_prim_number_combination(prim_num_list, exp):
    cls = problem060.problem_060()
    assert cls.is_quite_remarkable_prim_number_combination(list(prim_num_list)) == exp


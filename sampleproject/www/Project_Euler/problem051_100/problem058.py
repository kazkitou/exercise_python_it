"""Project Euler Problem 57"""
import itertools
import math


def problem_58() -> int:
    """Spiral primes"""
    numerator = 0
    denominator = 1
    for side in itertools.count(3, step=2):
        numerator += get_prim_number_length(get_diagonal_number(side))
        denominator += 4
        if (numerator / denominator) < 0.1:
            return side
    return -1


def get_diagonal_number(side: int) -> list():
    """一辺が引数{side}の四角形の角の値を返す"""
    if side == 1:
        return list([1])
    max_side = side**2
    sub = side -1
    return [max_side, max_side - sub, max_side - 2 * sub, max_side - 3 * sub]


def get_prim_number_length(num_list: list) -> int:
    """引数{num_list}内の素数の数を返す"""
    prim_num_list = [num for num in num_list if judge_prim_number(num)]
    return len(prim_num_list)


def judge_prim_number(num: int) -> bool:
    """
    引数{num}が素数か判断する
        True  -> 素数である
        False -> 素数でない
    """
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(problem_58())

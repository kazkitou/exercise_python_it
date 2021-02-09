"""Project Euler Problem 45"""
import itertools
import math


def problem_45() -> int:
    """Triangular, pentagonal, and hexagonal"""
    for i in itertools.count(144):
        hexagonal_num = i * (2 * i - 1)
        if judge_triangular_number(hexagonal_num) and judge_pentagonal_number(
            hexagonal_num
        ):
            return hexagonal_num
    return -1


def judge_triangular_number(num: int) -> bool:
    """
    引数numが三角数であるか判断する。
        True  -> 三角数である
        False -> 三角数でない
            n(n+1)/2 = num
            n**2 + n - 2num = 0
            n = (-1±√1+8num) / 2
            （n > 0 & nが整数 = Tn項の三角数）
    """
    return ((-1 + math.sqrt(1 + 8 * num)) / 2).is_integer()


def judge_pentagonal_number(num: int) -> bool:
    """
    引数numが五角数であるか判断する。
        True  -> 五角数である
        False -> 五角数でない
            n(3n-1)/2 = num
            3n**2 - n - 2num = 0
            n = (1±√1+24num) / 6
            （n > 0 & nが整数 = Pn項の五角数）
    """
    return ((1 + math.sqrt(1 + 24 * num)) / 6).is_integer()


if __name__ == "__main__":
    print(problem_45())

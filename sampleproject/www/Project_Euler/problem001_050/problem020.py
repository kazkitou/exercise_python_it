"""Project Euler Problem 20"""
from datetime import datetime, timedelta


def problem_20() -> int:
    """Factorial digit sum"""
    num_kai = number_kai(100)
    ret = sum(int(char) for char in str(num_kai))
    return ret


def number_kai(num: int) -> int:
    """
    n! = n * (n-1) * (n-2) * ... * 1
    """
    ret = 1
    for i in range(1, num + 1):
        ret *= i
    return ret


if __name__ == "__main__":
    print(problem_20())

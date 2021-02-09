"""Project Euler Problem 29"""
import math


def problem_29() -> int:
    """Distinct powers"""

    pow_set = set()
    for pow_a in range(2, 101):
        for pow_b in range(2, 101):
            pow_set.add(int(math.pow(pow_a, pow_b)))
    return len(pow_set)


if __name__ == "__main__":
    print(problem_29())

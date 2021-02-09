"""Project Euler Problem 27"""
import math
import itertools


def problem_27() -> int:
    """Quadratic primes"""
    seki_a_b = 0
    max_sqc_len = 0
    # n^2+an+b (|a| < 1000)
    for num_a in range(-999, 1000):
        # n^2+an+b (|b| <= 1000)
        for num_b in range(-1000, 1001):
            sqc_len = get_prim_number_sequence_length(num_a, num_b)
            if max_sqc_len < sqc_len:
                max_sqc_len = sqc_len
                seki_a_b = num_a * num_b
    return seki_a_b


def judge_prim_number(num: int) -> bool:
    """
    素数かどうか判定する。
        True  -> 素数である
        False -> 素数でない
    """
    if num < 0:
        num *= -1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


def get_prim_number_sequence_length(num_a: int, num_b: int) -> int:
    """
    引数(a, b)と以下の数式を用いて数値を作成する。
        n**2 + a*n + b
    nを0から加算していき作成した数値が素数であるか調べる。
    連続した素数が何回できるかを返す。
    """
    check_num = 0
    for num_n in itertools.count():
        check_num = num_n ** 2 + num_a * num_n + num_b
        if not judge_prim_number(check_num):
            return num_n
    return 0


if __name__ == "__main__":
    print(problem_27())

"""Project Euler Problem 36"""
import math


def problem_36() -> int:
    """Double-base palindromes"""
    palindrome = 0
    for i in range(1000000):
        if judge_palindrome_decimal(i) and judge_palindrome_bit(i):
            palindrome += i
    return palindrome


def judge_palindrome_decimal(num: int) -> bool:
    """
    引数numが10進数表記で回文であるか判断する
        True  -> 回文である
        False -> 回文でない
    """
    check_num = str(num)
    for i in range(math.ceil(len(check_num) / 2)):
        if check_num[i] != check_num[-(i + 1)]:
            return False
    return True


def judge_palindrome_bit(num: int) -> bool:
    """
    引数numが2進数表記で回文であるか判断する
        True  -> 回文である
        False -> 回文でない
    """
    check_num = bin(num)[2:]
    for i in range(math.ceil(len(check_num) / 2)):
        if check_num[i] != check_num[-(i + 1)]:
            return False
    return True


if __name__ == "__main__":
    print(problem_36())

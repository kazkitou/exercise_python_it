"""Project Euler Problem 43"""
import itertools
import math


def problem_43() -> int:
    """Sub-string divisibility"""
    sum_sub_string_divisibility_pandigital_num = 0
    for check_pandigital_num_list in itertools.permutations(list("0123456789")):
        check_pandigital_num = "".join(check_pandigital_num_list)
        if not judge_sub_string_divisibility_pandigital_number(check_pandigital_num):
            continue
        sum_sub_string_divisibility_pandigital_num += int(check_pandigital_num)
    return sum_sub_string_divisibility_pandigital_num


def judge_sub_string_divisibility_pandigital_number(pandigital_num: str) -> bool:
    """
    0から9のパンデジタル数の部分文字列が対象の素数で割り切れる数字か判断する。
    （引数pandigital_numはパンデジタル数であること前提）
        True  -> 割り切れる
        False -> 割り切れない

        ex) d1を上位1桁目, d2を上位2桁目の数とし, 以下順にdnを定義する. この記法を用いると次のことが分かる.
            d2 d3 d4 =406 は 2  で割り切れる
            d3 d4 d5 =063 は 3  で割り切れる
            d4 d5 d6 =635 は 5  で割り切れる
            d5 d6 d7 =357 は 7  で割り切れる
            d6 d7 d8 =572 は 11 で割り切れる
            d7 d8 d9 =728 は 13 で割り切れる
            d8 d9 d10=289 は 17 で割り切れる
    """
    for index in range(1, 8):
        if int(pandigital_num[index : index + 3]) % get_prim_number(index) != 0:
            return False
    return True


def get_prim_number(index: int) -> int:
    """
    引数index番目の素数を返す
    """
    for i in itertools.count(2):
        if judge_prim_number(i):
            index -= 1
            if index <= 0:
                return i
    return 0


def judge_prim_number(num: int) -> bool:
    """
    引数numが素数かどうか判断する
        True  -> 素数である
        False -> 素数でない
    """
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(problem_43())

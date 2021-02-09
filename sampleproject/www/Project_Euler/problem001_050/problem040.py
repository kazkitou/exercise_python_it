"""Project Euler Problem 40"""
import itertools


def problem_40() -> int:
    """Champernowne's constant"""
    champernowne_num_list = [1, 10, 100, 1000, 10000, 100000, 1000000]
    ret = 1
    for i in champernowne_num_list:
        ret *= get_digit_from_champernowne(i)
    return ret


def get_digit_from_champernowne(num: int) -> int:
    """
    チャンパーノウン定数から引数num桁目の数値を取得して返す
        ex) 引数num = 12の場合、以下の矢印部分を返す
            0.123456789101112
                         ↑
    """
    target_digit = None
    next_decimal = ""
    before_decimal_degit = 0
    for i in itertools.count(1):
        next_decimal = str(i)
        if before_decimal_degit + len(next_decimal) >= num:
            target_digit = int(next_decimal[num - before_decimal_degit - 1])
            break
        before_decimal_degit += len(next_decimal)
    return target_digit


if __name__ == "__main__":
    print(problem_40())

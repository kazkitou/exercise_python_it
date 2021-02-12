"""Project Euler Problem 57"""
import itertools
import math


def problem_57() -> int:
    """	Square root convergents"""
    counter = 0
    for i in itertools.count(1, 5):
        fraction_list = get_fraction(1, get_continued_fraction_expansion(i))
        print(fraction_list)
        if judge_numerator_digit_is_bigger_than_denominator(fraction_list):
            counter += 1
    return counter


def get_fraction(num: int, fraction_list: list) -> list:
    """a + b/c -> return fraction[a*c+b, c]"""
    print('get_fraction', num, fraction_list)
    tmp_list = [num*fraction_list[1]+fraction_list[0], fraction_list[1]]
    max_gcd = math.gcd(tmp_list[0], tmp_list[1])
    return list([tmp_list[0]//max_gcd, tmp_list[1]//max_gcd])


def get_continued_fraction_expansion(ex_cnt: int) -> list:
    """
    平方根の連分数展開の公式を用いて、√2をリスト形式で[分子, 分母]の値を返す
        ex_cnt == 1 -> 1 +                1/2
        ex_cnt == 2 -> 1 + 1/          (2+1/2)
        ex_cnt == 3 -> 1 + 1/     (2+1/(2+1/2))
        ex_cnt == 4 -> 1 + 1/(2+1/(2+1/(2+1/2)))
            計算を{ex_cnt}回繰り返して求めた値を返す
    """
    tmp_list = list()
    if ex_cnt <= 1:
        return list([1, 2])
    else:
        tmp_list = get_continued_fraction_expansion(ex_cnt-1)
    return get_fraction(2, list([tmp_list[1], tmp_list[0]]))


def judge_numerator_digit_is_bigger_than_denominator(fraction_list: list) -> bool:
    """
    fraction_list[0] = numerator
    fraction_list[1] = denominator
    return True = numerator digit is bigger than denominator. False = not True
    """
    return len(str(fraction_list[0])) > len(str(fraction_list[1]))


if __name__ == "__main__":
#    print(problem_57())
    print('last', get_fraction(1, get_continued_fraction_expansion(2)))

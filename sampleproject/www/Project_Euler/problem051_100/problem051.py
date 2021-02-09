"""Project Euler Problem 51"""
import itertools
import math


def problem_51() -> int:
    """Prime digit replacements"""
    rplc_char = "X"
    for max_digit in itertools.count(1):
        for rplc_digit in range(1, max_digit):
            check_list = get_prime_digit_replacements_check_list(
                max_digit, rplc_char, rplc_digit
            )
            for num_list in check_list:
                num_str = "".join(num_list)
                prim_num_list = get_prim_number_replace_number(num_str, rplc_char)
                if len(prim_num_list) == 8:
                    return prim_num_list[0]
    return -1


def get_prime_digit_replacements_check_list(
    max_digit: int, rplc_char, rplc_digit: int
) -> list:
    """
    Return Check Number List (String)
        {rplc_char} * {rplc_digit} replace digit in {max_digit} digit
    """
    pattern_list = [str(i) for i in range(10)]
    pattern_list.append(rplc_char)
    check_list = [
        num
        for num in itertools.product(pattern_list, repeat=max_digit)
        if num.count(rplc_char) == rplc_digit
    ]
    return check_list


def get_prim_number_replace_number(check_num_str: str, rplc_char: str) -> list:
    """
    Return Prim Number List (Integer) : {rplc_char} digit replace Number
    """
    prim_num_list = list()
    for rplace_num in range(10):
        check_num = int(check_num_str.replace(rplc_char, str(rplace_num)))
        if len(str(check_num)) != len(check_num_str):
            # 先頭が0の場合は桁数が変わるため、確認対象外とする
            continue
        if judge_prim_number(check_num):
            prim_num_list.append(check_num)
    return prim_num_list


def judge_prim_number(num: int) -> bool:
    """Return bool : {num} is Prim Number?"""
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(problem_51())

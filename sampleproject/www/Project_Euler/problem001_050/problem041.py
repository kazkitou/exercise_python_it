"""Project Euler Problem 41"""
import math
import itertools


def problem_41() -> int:
    """Pandigital prime"""
    pandigital_max_list = "123456789"
    for i in range(len(pandigital_max_list), 0, -1):
        # 数の大きいほうからチェックしたいため、桁分を抽出して前後反転（大きいほうの数字を先頭に変換）する
        pandigital_list = list(pandigital_max_list[:i][::-1])
        # itertools.permutationsで大きいほうの数字からチェックできる形のリストを引数にして組み合わせる
        for check_num_list in itertools.permutations(pandigital_list):
            check_num = int("".join(check_num_list))
            if judge_pandigital_digit(check_num) and judge_prim_number(check_num):
                return check_num
    return 0


def judge_pandigital_digit(num: int) -> bool:
    """
    引数numがパンデジタルかどうか判断する
    (ここでのパンデジタルとは、Project Euler Problem 41で指定されたもの)
        True  -> パンデジタルである
        False -> パンデジタルでない
    """
    check_digit = list("123456789"[: len(str(num))])
    if sorted(str(num)) == check_digit:
        return True
    return False


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
    print(problem_41())

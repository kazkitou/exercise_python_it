"""Project Euler Problem 49"""
import math
import itertools


def problem_49() -> str:
    """Prime permutations"""
    check_list = list()
    exclude_list = [1487, 4817, 8147]
    for base in range(1, 10000):
        for tolerance in itertools.count(1):
            check_list = [base, base + tolerance * 1, base + tolerance * 2]
            if (
                min(check_list) < 1000
                or max(check_list) > 9999
                or check_list == exclude_list
            ):
                break
            if judge_cycle_number_list(check_list) and judge_prim_number_list(
                check_list
            ):
                return str(check_list[0]) + str(check_list[1]) + str(check_list[2])
    return "None"


def judge_cycle_number_list(num_list: list) -> bool:
    """
    引数num_list内の数字が全て、各項が他の項の置換で表される数字であるか判断する
        True  -> 各項が他の項の置換で表される
        False -> 少なくとも1つは、各項が他の項の置換で表されない
    """
    chrck_cycle_num = sorted(str(num_list[0]))
    for check_num in num_list:
        if chrck_cycle_num != sorted(str(check_num)):
            return False
    return True


def judge_prim_number_list(num_list: list) -> bool:
    """
    引数num_list内の数字が全て素数であるか判断する
        True  -> 全て素数である
        False -> 少なくとも1つは素数でない
    """
    for num in num_list:
        if not judge_prim_number(num):
            return False
    return True


def judge_prim_number(num: int) -> bool:
    """
    引数numが素数であるか判断する
        True  -> 素数である
        False -> 素数でない
    """
    for i in range(3, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(problem_49())

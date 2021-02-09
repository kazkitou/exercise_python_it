"""Project Euler Problem 35"""
import math


def problem_35() -> int:
    """Circular primes"""
    # 100万未満の値は 0 ～ 999999 -> 6桁の数字[0, 1, 2, ... , 9]の組み合わせ
    circle_prim_num = [2]
    for i in range(3, 1000000, 2):
        if judge_circle_prim_number(i):
            circle_prim_num.append(int(i))
    return len(circle_prim_num)


def judge_circle_prim_number(num: int) -> bool:
    """
    引数numが巡回素数であるか判断する。
        True  -> 巡回素数である
        False -> 巡回素数でない
    """
    for pattern_num in range(len(str(num))):
        check_num = get_cycle_number(num, pattern_num)
        if not check_prim_number(check_num):
            return False
    return True


def get_cycle_number(num: int, cycle_num: int) -> int:
    """
    引数numを左方向へ引数cycle_num回 回転させた値を返す
        引数num = abcde, 引数cycle_num = 3
        return deabc
    """
    num_str = str(num)
    left_num_str = num_str[cycle_num : len(num_str)]
    right_num_str = num_str[0:cycle_num]
    return int(left_num_str + right_num_str)


def check_prim_number(num: int) -> bool:
    """
    引数numが素数であるか判断する。
        True  -> 素数である
        False -> 素数でない
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(problem_35())

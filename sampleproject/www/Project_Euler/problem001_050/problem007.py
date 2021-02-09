"""Project Euler Problem 7"""


def problem_7() -> int:
    """10001st prime"""
    # 6番目の素数が13であることを確かめることから開始する
    check_num = 13
    check_cnt = 5
    while True:
        if judge_prime_number(check_num):
            check_cnt += 1
            if check_cnt >= 10001:
                break
        check_num += 2
    return check_num


def judge_prime_number(num: int) -> bool:
    """
    Judge Prim Number
        True  -> Prim Number
        False -> Not Prim Number
    """
    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print(problem_7())

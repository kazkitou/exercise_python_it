"""Project Euler Problem 21"""


def problem_21() -> int:
    """Amicable numbers"""
    sum_amicable_number = 0
    target_num = 0
    tmp_a = 0
    tmp_b = 0
    for chk in range(1, 10000):
        target_num = chk
        tmp_a = sum(filter(lambda num: target_num % num == 0, range(1, target_num)))
        tmp_b = sum(filter(lambda num: tmp_a % num == 0, range(1, tmp_a)))
        if chk != tmp_a and chk == tmp_b:
            sum_amicable_number += chk
    return sum_amicable_number


if __name__ == "__main__":
    print(problem_21())

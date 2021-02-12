"""Project Euler Problem 56"""


def problem_56() -> int:
    """Powerful digit sum"""
    sum_digit_num_list = list()
    for num_a in range(1, 100):
        for num_b in range(1, 100):
            sum_digit_num_list.append(get_sum_digit_number(num_a ** num_b))
    return max(sum_digit_num_list)


def get_sum_digit_number(num: int) -> int:
    """return sum all digit"""
    return sum(list([int(digit) for digit in str(num)]))


if __name__ == "__main__":
    print(problem_56())

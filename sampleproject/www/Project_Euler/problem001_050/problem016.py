"""Project Euler Problem 16"""


def problem_16() -> int:
    """Power digit sum"""
    num = 1
    cnt = 0
    while cnt < 1000:
        num *= 2
        cnt += 1
    pow_str = str(num)

    ret = 0
    for str_num in pow_str:
        ret += int(str_num)

    return ret


if __name__ == "__main__":
    print(problem_16())

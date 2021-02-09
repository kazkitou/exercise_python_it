"""Project Euler Problem 4"""


def problem_4() -> int:
    """	Largest palindrome product"""
    ret = 0
    calc_max = 0
    tmp = ""
    for cnt_left in range(1, 999):
        for cnt_right in range(1, 999):
            if calc_max > (cnt_left * cnt_right):
                continue
            tmp = "{:0>4}".format(cnt_left * cnt_right)
            if tmp != tmp[::-1]:
                continue
            calc_max = cnt_left * cnt_right
    ret = calc_max
    return ret


if __name__ == "__main__":
    print(problem_4())

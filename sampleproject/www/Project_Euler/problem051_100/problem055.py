"""Project Euler Problem 55"""


def problem_55() -> int:
    """Lychrel numbers"""
    lychrel_number_list = list()
    for i in range(1, 10000):
        tmp_num = i
        loop_cnt = 1
        while loop_cnt < 50:
            tmp_num = get_sum_reverse_number(tmp_num)
            if judge_palindrome_number(tmp_num):
                break
            loop_cnt += 1
        if loop_cnt == 50:
            lychrel_number_list.append(i)
    return len(lychrel_number_list)


def get_sum_reverse_number(num: int) -> int:
    """return {num} + reverse {num}"""
    return num + int(str(num)[::-1])


def judge_palindrome_number(num: int) -> bool:
    """return True(equal palindrome) or False(not palindrome)"""
    return str(num) == str(num)[::-1]


if __name__ == "__main__":
    print(problem_55())

"""Project Euler Problem 5"""


def problem_5() -> int:
    """Smallest multiple"""
    ret = 0
    div_max = 20
    div_list = list(range(1, div_max + 1))

    #   1～20の最小公倍数を求める。（外部ライブラリがありそう・・・）
    #   一部の値は考慮不要であるため除外する。
    #   例) 20の最小公倍数が考慮に含まれていれば、1,2,4,5,10は考慮不要
    #       1 × 20 = 20, 2 × 10 = 20, 4 × 5 = 20
    for i in range(div_max, 0, -1):
        for j in range(1, i):
            if i % j == 0:
                if j in div_list:
                    div_list.remove(j)

    min_num = max(div_list)
    while True:
        tmp = min_num
        for divide in div_list:
            if not min_num % divide == 0:
                min_num += max(div_list)
                continue
        if tmp == min_num:
            break
    ret = min_num
    return ret


if __name__ == "__main__":
    print(problem_5())

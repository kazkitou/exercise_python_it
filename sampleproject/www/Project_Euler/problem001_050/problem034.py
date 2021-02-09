"""Project Euler Problem 34"""


def problem_34() -> int:
    """Digit factorials"""
    # 最大数は9!を桁数分加算した値となる（9! = 362880）
    # 6桁 [ 0 ~   999999] -> 9! * 6 = 2177280
    # 7桁 [ 0 ~  9999999] -> 9! * 7 = 2540160
    # 7桁で表現できる最大値(9999999)が、各桁階乗の最大値(9! * 7)を加算した値を超える。
    # そのため調査する最大値は7桁で最大となる値までとなる。
    # 1!と2!は総和に含めてはならないため、最小値は3!となる。
    ret = 0
    for i in range(3, 2540160 + 1):
        check_kaijo = 0
        for num_char in str(i):
            check_kaijo += get_num_kaijo_special(int(num_char))
        if i == check_kaijo:
            ret += i
    return ret


def get_num_kaijo_special(num: int) -> int:
    """
    引数numの階乗の値を返す
    """
    kaijo = 1
    # 0! = 1
    if num == 0:
        return 1
    # 引数numが1桁でない場合は異常値とみなす。
    if num < 1 or num > 9:
        return 0
    for i in range(num, 0, -1):
        kaijo *= i
    return kaijo


if __name__ == "__main__":
    print(problem_34())

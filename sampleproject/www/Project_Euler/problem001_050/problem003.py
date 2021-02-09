"""Project Euler Problem 3"""


def problem_3() -> int:
    """Largest prime factor"""
    surplus = trial_division(600851475143)
    print("prim factor = {}".format(str(surplus)))
    ret = max(surplus)
    return ret


def trial_division(num: int) -> list:
    """
    試し割り法で、nまでの素因数を返す
    """
    ret = []
    calc_tmp = num
    for i in range(2, num):
        if i * i > num:
            #   nが2で割り切れる場合、4の場合を調べる必要はない。（p*2の値も抽出される場合は素数ではない）
            #   n = p * qでqが1を超える場合は、上記の考えから既に抽出済み。
            #   qが1未満でよいので最大でもp * pがn未満の値まで調べればよい。
            break
        if not judge_prim_number(i):
            #   素数以外の値は考慮しない
            continue
        if calc_tmp % i == 0:
            while calc_tmp % i == 0:
                ret.append(i)
                calc_tmp //= i
    return ret


def judge_prim_number(check_num: int) -> bool:
    """
    nが素数か判定する
        True  -> 素数である
        False -> 素数でない
    """
    for i in range(2, check_num):
        if i * i > check_num:
            break
        if check_num % i == 0:
            return False
    return True


if __name__ == "__main__":
    print("Largest prime factor = {}".format(str(problem_3())))

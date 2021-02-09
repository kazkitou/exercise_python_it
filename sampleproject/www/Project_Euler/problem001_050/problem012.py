"""Project Euler Problem 12"""


def problem_12() -> int:
    """Highly divisible triangular number"""
    tri_cnt = 1
    tri_num = 0
    while True:
        tri_num = tri_cnt * (tri_cnt + 1) / 2
        if get_division_count(tri_num) > 500:
            break
        tri_cnt += 1
    return tri_num


def get_division_count(num: float) -> int:
    """
    素因数分解を行い、各因子の個数を求める。
    自然数は必ず素数の掛け算で表現できる？
        input
            num -> num = P1 * P2 * P3 * ... * Pn
                p = 素因数分解した各項
        output
            ret -> numの約数の個数を求めるアルゴリズムに従う
                (P1の乗数+1) * (P2の乗数+1) * (P2の乗数+1) * ... * (Pnの乗数+1)
    """
    ret = 1
    div_val = 2
    tmp = num
    while tmp != 1:
        div_cnt = 1
        while tmp % div_val == 0:
            tmp /= div_val
            div_cnt += 1
        ret *= div_cnt
        div_val += 1
    return ret


if __name__ == "__main__":
    print(problem_12())

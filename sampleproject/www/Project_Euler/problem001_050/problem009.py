"""Project Euler Problem 9

    pytestを用いたテスト自動化を試したい。
    そのため入出力行う関数を作成する。

    [問題]
        ピタゴラス数(ピタゴラスの定理を満たす自然数)とは a < b < c で以下の式を満たす数の組である.
            ピタゴラスの定理：直角三角形はa^2 + b^2 = c^2
            例えば, 3^2 + 4^2 = 9 + 16 = 25 = 5^2 である.(a=3, b=4, c=5)
        a + b + c = 1000 となるピタゴラスの三つ組が一つだけ存在する.
        これらの積 abc を計算しなさい.
            1.  main関数(a, b, cの組み合わせをつくり各関数を使用する)
                input   なし
                output  int
            2.  引数a, b, cがピタゴラスの定理に当てはまるか判断する
                input   int a, b, c
                output  boolean
            3.  引数a, b, cの積を求める
                input   list
                output  int
"""


def problem_9() -> int:
    """
    Special Pythagorean triplet
    1.  main関数(a, b, cの組み合わせをつくり各関数を使用する)
    """
    product_a_b_c = 0
    max_count = 1000
    for cnt_a in range(1, max_count + 1):
        for cnt_b in range(cnt_a + 1, max_count + 1):
            cnt_c = max_count - cnt_a - cnt_b
            if (cnt_c < 0) or (cnt_c <= cnt_a) or (cnt_c <= cnt_b):
                continue
            if judge_pythagorean(cnt_a, cnt_b, cnt_c):
                product_a_b_c = calc_product([cnt_a, cnt_b, cnt_c])
    return product_a_b_c


def judge_pythagorean(cnt_a: int, cnt_b: int, cnt_c: int) -> bool:
    """
    引数a, b, cがピタゴラスの定理に当てはまるか判断する
    """
    judge = False
    if (cnt_a * cnt_a + cnt_b * cnt_b) == cnt_c * cnt_c:
        judge = True
    return judge


def calc_product(cnt_item: list) -> int:
    """
    引数a, b, cの積を求める
    """
    ret = 1
    for num in cnt_item:
        ret *= num
    print(cnt_item, ret)
    return ret


if __name__ == "__main__":
    print(problem_9())

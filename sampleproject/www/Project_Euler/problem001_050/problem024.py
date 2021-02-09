"""Project Euler Problem 24"""


def problem_24() -> str:
    """Lexicographic permutations"""
    target_num = 1000000
    pattern_list = list(range(10))
    ret = search_pattern(target_num, pattern_list)

    return ret


def search_pattern(target_num: int, select_list: list) -> str:
    """
    select_list内データを1つずつ使用した数字を辞書順に並べた際にtarget_num番目の数字を返す。
    使用した数字は再度使用できない。辞書順のため大きい桁にある数字が小さいほうから順に並べられる。
    X桁の選択パターンがtarget_numを越えるタイミングを見つける。
        ex)
            10個の数字の10桁の組み合わせパターンは10!通り。
            9桁以降の組み合わせは9!通り、8桁以降の組み合わせは8!通り、 ... 2桁以降の組み合わせは2!通り、1桁の組み合わせは1!通り。
    辞書順のため大きい桁に小さい値を設定した場合の動作を感が会える。
    X桁目の値は、X-1桁のパターン数がtarget_numに何回入るかで決まる。
        ex) リスト[0, 1, 2]の組み合わせの4番目の数値の場合
            3桁目の値は、2桁目のパターン数が2通り(2!通り)のであり、4番目に2回入る。
            そのため3桁目の値はリスト内2番目値である1になる。
    上記を再帰処理として繰り返すことでtarget_num番目の値を求める。

    作成後追記
        target_numが0以下の場合は1と同等の動きをする。
    """
    if len(select_list) == 0:
        # 再帰関数であり、選択肢がなくなると終了
        return ""
    if target_num > number_kai(len(select_list)):
        # target_num番目のパターンがない。（全組み合わせパターンを超える値を要求される）
        return "out of range : target number"

    select_list.sort()
    next_keta_pattern_num = number_kai(len(select_list) - 1)
    select_num = ""
    for i in range(len(select_list)):
        if target_num <= next_keta_pattern_num * (i + 1):
            select_num = str(select_list.pop(i))
            return select_num + search_pattern(
                target_num - next_keta_pattern_num * i, select_list
            )

    return "Error"


def number_kai(num: int) -> int:
    """
    n! = n * (n-1) * (n-2) * ... * 1
    """
    ret = 1
    for i in range(1, num + 1):
        ret *= i
    return ret


if __name__ == "__main__":
    print(problem_24())

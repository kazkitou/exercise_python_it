"""Project Euler Problem 32"""


def problem_32() -> int:
    """Pandigital products"""
    pandigital_products_set = set()
    # 計算式「a × b = c」でb = 1の場合「5桁 × 1 = 5桁」だと合計で11桁になるためNG
    # 計算式「a × b = c」でb = 1の場合「4桁 × 1 = 4桁」だと合計で9桁になるためOK
    # a or b は4桁(9999)が最大とみなせる
    for i in range(1, 10000):
        for j in range(1, 10000):
            if len(str(i) + str(j) + str(i * j)) > 9:
                # 1度でも9桁を超えると、それ以降9桁以内になることはないと考えた
                break
            if check_pandigital_products(i, j):
                # 積が同じ値の場合は1回のみ計上
                pandigital_products_set.add(i * j)
    return sum(pandigital_products_set)


def check_pandigital_products(left_num: int, right_num: int) -> bool:
    """
    計算式「a × b = c」のa, b, cが1, 2, 3, ... , 9で構成されているか確認する
    （計算式の値がパンデジタルであるか確認する）
        ex1) 39 × 186 = 7254 -> True
            この時引数 left_num = 39, right_num = 186
        ex2) 40 × 186 = 7440 -> False
            この時引数 left_num = 40, right_num = 186
    """
    check_num = get_dictionary_char(
        str(left_num) + str(right_num) + str(left_num * right_num)
    )

    # パンデジタルであるか判断する
    if check_num == get_dictionary_char("123456789"):
        return True

    return False


def get_dictionary_char(original_str: str) -> dict:
    """
    引数original_strを1文字ずつ辞書データに入れ込む。
        key   -> 1文字
        value -> keyが使用されている回数
    """
    ret = {}
    for i in original_str:
        ret[i] = ret.get(i, 0) + 1
    return ret


if __name__ == "__main__":
    print(problem_32())

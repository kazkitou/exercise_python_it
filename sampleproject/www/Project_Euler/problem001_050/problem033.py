"""Project Euler Problem 33"""


def problem_33() -> int:
    """Digit cancelling fractions"""
    funny_fraction_list = list()
    for div_mother in range(10, 100):
        for div_child in range(10, div_mother):
            # 自明である or 自明でない ----> 約分した結果に等しい or 等しくない
            for calc_div_child, calc_div_mother in get_pattern_simple_funny_fraction(
                div_child, div_mother
            ):
                if judge_funny_fraction(
                    div_child, div_mother, calc_div_child, calc_div_mother
                ):
                    funny_fraction_list.append([div_child, div_mother])
    # 面白い分数の分子, 分母の積を算出
    ret_child = 1
    ret_mother = 1
    for funny_fraction_child, funny_fraction_mother in funny_fraction_list:
        ret_child *= funny_fraction_child
        ret_mother *= funny_fraction_mother
    # 面白い分数の、分子の積 / 分母の積 を約分する
    for i in range(max(ret_child, ret_mother), 0, -1):
        if (ret_child % i == 0) and (ret_mother % i == 0):
            ret_child //= i
            ret_mother //= i
            break
    return ret_mother


def get_pattern_simple_funny_fraction(div_child: int, div_mother: int) -> list:
    """
    簡単な形にすることのできる分数に対して、今後に計算が必要なパターンを返す
    """
    ret = list()
    # 自明である or 自明でない ----> 約分した結果に等しい or 等しくない
    # a*/a* -> 値の等しい桁が分子、分母でそれぞれ1, 1
    if div_child % 10 == div_mother % 10:
        ret.append([div_child // 10, div_mother // 10])
    # a*/*a -> 値の等しい桁が分子、分母でそれぞれ1, 2
    if div_child % 10 == div_mother // 10:
        ret.append([div_child // 10, div_mother % 10])
    # *a/a* -> 値の等しい桁が分子、分母でそれぞれ2, 1
    if div_child // 10 == div_mother % 10:
        ret.append([div_child % 10, div_mother // 10])
    # *a/*a -> 値の等しい桁が分子、分母でそれぞれ2, 2
    if div_child // 10 == div_mother // 10:
        ret.append([div_child % 10, div_mother % 10])
    return ret


def judge_funny_fraction(
    div_child: int,
    div_mother: int,
    div_child_fny: int,
    div_mother_fny: int,
) -> bool:
    """
    面白い分数であるか判断する。（Project Euler Problem 33を参照）
        True  -> 面白い分数である
        False -> 面白い分数でない
    """
    # 0 除算のチェック
    if div_mother <= 0 or div_mother_fny <= 0:
        return False

    # 自明な分数か判断する
    if judge_reduction_of_fraction(
        div_child, div_mother, div_child_fny, div_mother_fny
    ):
        return False

    # 分数比較
    if (div_child / div_mother) == (div_child_fny / div_mother_fny):
        return True
    return False


def judge_reduction_of_fraction(
    div_child: int,
    div_mother: int,
    div_child_fny: int,
    div_mother_fny: int,
) -> bool:
    """
    自明な分数であるか判断する。（Project Euler Problem 33を参照）
        True  -> 自明な分数である
        False -> 自明な分数でない
    """
    # 0 除算のチェック
    if div_mother <= 0 or div_mother_fny <= 0:
        return False

    if (div_child % 10 == 0) and (div_mother % 10 == 0):
        if (div_child // 10 == div_child_fny) or (div_mother // 10 == div_mother_fny):
            return True

    return False


if __name__ == "__main__":
    print(problem_33())

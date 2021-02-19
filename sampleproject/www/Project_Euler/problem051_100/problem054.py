"""Project Euler Problem 54
    ポーカーでの勝敗に関するモジュール
"""

# 訳注 : この問題に置いてA 2 3 4 5というストレートは考えなくてもよい
cards_num_dict = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

# 関数をリストとして保持したいため、対象関数をリストの前に記載する
def get_poker_hands_no_role(hands_num: list, hands_suit: list) -> int:
    """ポーカーの役無し
    引数からポーカーの手札の中で最も大きいカードを返す
    Args:
        hands_num   (list)  :   手札のトランプに表示されている数値
        hands_suit  (list)  :   手札のトランプに表示されているマーク
    Returns:
        int :   手札の最大数値
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> get_poker_hands_no_role([1,2,3], [])
        3
        >>> get_poker_hands_no_role([], [])
        ？
    Note:
        引数がlist()の場合の動作不明
    """
    return max(hands_num)


def get_poker_hands_one_pair(hands_num: list, hands_suit: list) -> int:
    """
    引数からポーカーのワンペアであるかどうか、またそのカードの数値を返す
    Args:
        hands_num   (list)  :   手札のトランプに表示されている数値
        hands_suit  (list)  :   手札のトランプに表示されているマーク
    Returns:
        int :   ワンペアの数値 （== 0 : 1ペアでない、!= 0 : 1ペアである）
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> get_poker_hands_one_pair([1, 2, 3, 6, 6], [])
        6
        >>> get_poker_hands_one_pair([4, 5, 6, 7, 8], [])
        0
    Note:
        引数がlist()の場合の動作不明
    """
    for num in hands_num:
        if hands_num.count(num) == 2:
            return num
    return 0


def get_poker_hands_two_pair(hands_num: list, hands_suit: list) -> int:
    """
    引数からポーカーのツーペアであるかどうか、またペアカードの最大数値を返す
    Args:
        hands_num   (list)  :   手札のトランプに表示されている数値
        hands_suit  (list)  :   手札のトランプに表示されているマーク
    Returns:
        int :   ペアの最大数値 （== 0 : 2ペアでない、!= 0 : 2ペアである）
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> get_poker_hands_two_pair([1, 3, 3, 6, 6], [])
        6
        >>> get_poker_hands_two_pair([4, 5, 6, 6, 8], [])
        0
    Note:
        引数がlist()の場合の動作不明
    """
    one_pair_num = get_poker_hands_one_pair(hands_num, hands_suit)
    two_pair_num = get_poker_hands_one_pair(
        list(filter(lambda x: x != one_pair_num, hands_num)), hands_suit
    )

    max_num = max(one_pair_num, two_pair_num) if two_pair_num != 0 else 0
    return max_num


def get_poker_hands_three_cards(hands_num: list, hands_suit: list) -> int:
    """
    引数からポーカーのスリーカードであるかどうか、また3枚揃っているカードの最大数値を返す
    Args:
        hands_num   (list)  :   手札のトランプに表示されている数値
        hands_suit  (list)  :   手札のトランプに表示されているマーク
    Returns:
        int :   ペアの最大数値 （== 0 : 3カードでない、!= 0 : 3カードである）
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> get_poker_hands_three_cards([1, 3, 3, 3, 6], [])
        3
        >>> get_poker_hands_three_cards([4, 5, 6, 6, 8], [])
        0
    Note:
        引数がlist()の場合の動作不明
    """
    for num in hands_num:
        if hands_num.count(num) == 3:
            return num
    return 0


def get_poker_hands_strait(hands_num: list, hands_suit: list) -> int:
    """
    引数からポーカーのストレートであるかどうか、またカードの最大数値を返す
    Args:
        hands_num   (list)  :   手札のトランプに表示されている数値
        hands_suit  (list)  :   手札のトランプに表示されているマーク
    Returns:
        int :   ペアの最大数値 （== 0 : ストレートでない、!= 0 : ストレートである）
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> get_poker_hands_strait(2, 3, 4, 5, 6], [])
        6
        >>> get_poker_hands_strait([4, 5, 6, 6, 8], [])
        0
    Note:
        引数がlist()の場合の動作不明
        この問題に置いてA 2 3 4 5というストレートは考えなくてもよい
    """
    for i in range(len(hands_num) - 1):
        if sorted(hands_num)[i] + 1 != sorted(hands_num)[i + 1]:
            return 0
    return max(hands_num)


def get_poker_hands_flash(hands_num: list, hands_suit: list) -> int:
    """
    引数からポーカーのフラッシュであるかどうか、またカードの最大数値を返す
    Args:
        hands_num   (list)  :   手札のトランプに表示されている数値
        hands_suit  (list)  :   手札のトランプに表示されているマーク
    Returns:
        int :   カードの最大数値 （== 0 : フラッシュでない、!= 0 : フラッシュである）
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> get_poker_hands_flash([2, 3, 4, 5, 6], ["C", "C", "C", "C", "C"])
        6
        >>> get_poker_hands_flash([2, 3, 4, 5, 6], ["C", "C", "C", "C", "D"])
        0
    Note:
        引数がlist()の場合の動作不明
    """
    if len(set(hands_suit)) == 1:
        return max(hands_num)
    return 0


def get_poker_hands_fullhouse(hands_num: list, hands_suit: list) -> int:
    """
    引数からポーカーのフルハウスであるかどうか、また3枚揃っているカードの最大数値を返す
    Args:
        hands_num   (list)  :   手札のトランプに表示されている数値
        hands_suit  (list)  :   手札のトランプに表示されているマーク
    Returns:
        int :   3枚揃っているカードの最大数値 （== 0 : フルハウスでない、!= 0 : フルハウスである）
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> get_poker_hands_fullhouse([2, 2, 2, 4, 4], [])
        2
        >>> get_poker_hands_fullhouse([2, 2, 2, 4, 5], [])
        0
    Note:
        引数がlist()の場合の動作不明
    """
    three_card_num = get_poker_hands_three_cards(hands_num, hands_suit)
    one_pair_num = get_poker_hands_one_pair(
        list(filter(lambda x: x != three_card_num, hands_num)), hands_suit
    )

    max_num = three_card_num if one_pair_num != 0 and three_card_num != 0 else 0
    return max_num


def get_poker_hands_four_cards(hands_num: list, hands_suit: list) -> int:
    """
    引数からポーカーのフォーカードであるかどうか、またペアカードの最大数値を返す
    Args:
        hands_num   (list)  :   手札のトランプに表示されている数値
        hands_suit  (list)  :   手札のトランプに表示されているマーク
    Returns:
        int :   4枚揃っているカードの最大数値 （== 0 : フォーカードでない、!= 0 : フォーカードである）
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> get_poker_hands_four_cards([2, 2, 2, 2, 4], [])
        2
        >>> get_poker_hands_four_cards([2, 2, 2, 3, 4], [])
        0
    Note:
        引数がlist()の場合の動作不明
    """
    for num in hands_num:
        if hands_num.count(num) == 4:
            return num
    return 0


def get_poker_hands_strait_flash(hands_num: list, hands_suit: list) -> int:
    """
    引数からポーカーのストレートフラッシュであるかどうか、またカードの最大数値を返す
    Args:
        hands_num   (list)  :   手札のトランプに表示されている数値
        hands_suit  (list)  :   手札のトランプに表示されているマーク
    Returns:
        int :   カードの最大数値 （== 0 : ストレートフラッシュでない、!= 0 : ストレートフラッシュである）
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> get_poker_hands_strait_flash([3, 4, 5, 6, 7], ["H", "H", "H", "H", "H"])
        7
        >>> get_poker_hands_strait_flash([3, 4, 5, 6, 7], ["H", "H", "H", "H", "C"])
        0
        >>> get_poker_hands_strait_flash([3, 4, 5, 5, 7], ["H", "H", "H", "H", "H"])
        0
    Note:
        引数がlist()の場合の動作不明
        この問題に置いてA 2 3 4 5というストレートは考えなくてもよい
    """
    strait_num = get_poker_hands_strait(hands_num, hands_suit)
    flash_num = get_poker_hands_flash(hands_num, hands_suit)
    max_num = max(strait_num, flash_num) if min(strait_num, flash_num) != 0 else 0
    return max_num


def get_poker_hands_royal_flash(hands_num: list, hands_suit: list) -> int:
    """
    引数からポーカーのロイヤルフラッシュであるかどうか、またカードの最大数値を返す
    Args:
        hands_num   (list)  :   手札のトランプに表示されている数値
        hands_suit  (list)  :   手札のトランプに表示されているマーク
    Returns:
        int :   カードの最大数値 （== 0 : ロイヤルフラッシュでない、!= 0 : ロイヤルフラッシュである）
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> get_poker_hands_royal_flash([10, 11, 12, 13, 14], ["H", "H", "H", "H", "H"])
        7
        >>> get_poker_hands_royal_flash([10, 11, 12, 13, 14], ["H", "H", "H", "H", "S"])
        0
        >>> get_poker_hands_royal_flash([11, 11, 12, 13, 14], ["H", "H", "H", "H", "H"])
        0
    Note:
        引数がlist()の場合の動作不明
        この問題に置いてA 2 3 4 5というストレートは考えなくてもよい
    """
    strait_num = get_poker_hands_strait_flash(hands_num, hands_suit)
    if strait_num == cards_num_dict["A"]:
        return max(hands_num)
    return 0


# 手札のチェック順（弱い役から並べ、添え字の数値が高いほうが強い手札となる）
role_rank_func = [
    get_poker_hands_no_role,
    get_poker_hands_one_pair,
    get_poker_hands_two_pair,
    get_poker_hands_three_cards,
    get_poker_hands_strait,
    get_poker_hands_flash,
    get_poker_hands_fullhouse,
    get_poker_hands_four_cards,
    get_poker_hands_strait_flash,
    get_poker_hands_royal_flash,
]


def problem_54() -> int:
    """Poker hands"""
    p_one_wins = 0
    with open("p054_poker.txt", "rt") as file_p:
        read_lines = file_p.readlines()
    for cards in read_lines:
        if len(cards) < 2:
            continue
        player_one = cards[: len(cards) // 2].split()
        player_two = cards[len(cards) // 2 :].split()
        if judge_win_poker_player(player_one, player_two):
            p_one_wins += 1
    return p_one_wins


def judge_win_poker_player(p_one: list, p_two: list) -> bool:
    """
    引数p_oneと引数p_twoの手札でポーカーをし、引数p_oneの手札が勝つかどうか判断する
    Args:
        p_one   (list)  :   プレイヤー1の手札（数値 & マーク）
        p_two   (list)  :   プレイヤー2の手札（数値 & マーク）
    Returns:
        bool    :   プレイヤー1が勝ったかどうか （True : プレイヤー1の勝ちである、False : プレイヤー1の勝ちではない）
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> judge_win_poker_player(["5H", "5C", "6S", "7S", "KD"], ["2C", "3S", "8S", "8D", "TD"])
        False
        >>> judge_win_poker_player(["5D", "8C", "9S", "JS", "AC"], ["2C", "5C", "7D", "8S", "QH"])
        True
        >>> judge_win_poker_player(["2D", "9C", "AS", "AH", "AC"], ["3D", "6D", "7D", "TD", "QD"])
        False
        >>> judge_win_poker_player(["4D", "6S", "9H", "QH", "QC"], ["3D", "6D", "7H", "QD", "QS"])
        True
        >>> judge_win_poker_player(["2H", "2D", "4C", "4D", "4S"], ["3C", "3D", "3S", "9S", "9D"])
        True
    Note:
        引数がlist()の場合の動作不明
    """
    p_one_role, p_one_max_card_num = list(get_poker_hands(p_one).items())[0]
    p_two_role, p_two_max_card_num = list(get_poker_hands(p_two).items())[0]
    if p_one_role > p_two_role:
        return True
    if p_one_role == p_two_role:
        if p_one_max_card_num > p_two_max_card_num:
            return True
    return False


def get_poker_hands(hands: list) -> dict:
    """
    引数(5枚の手札)からポーカーの役と役の中で最も大きいカードを返す
    Args:
        hands   (list)  :   プレイヤーの手札（数値 & マーク）
    Returns:
        dict    :   手札の役の強さと役の中での最大数値({役の強さ, 最も大きいカードの値})
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> judge_win_poker_player(["5H", "5C", "6S", "7S", "KD"])
        {1 : 5}
        >>> judge_win_poker_player(["2C", "3S", "8S", "8D", "TD"])
        {1 : 8}
        >>> judge_win_poker_player(["5D", "8C", "9S", "JS", "AC"])
        {0 : 14}
        >>> judge_win_poker_player(["2C", "5C", "7D", "8S", "QH"])
        {0 : 12}
        >>> judge_win_poker_player(["2D", "9C", "AS", "AH", "AC"])
        {3 : 14}
        >>> judge_win_poker_player(["3D", "6D", "7D", "TD", "QD"])
        {5 : 12}
        >>> judge_win_poker_player(["4D", "6S", "9H", "QH", "QC"])
        {1 : 12}
        >>> judge_win_poker_player(["3D", "6D", "7H", "QD", "QS"])
        {1 : 12}
        >>> judge_win_poker_player(["2H", "2D", "4C", "4D", "4S"])
        {6 : 4}
        >>> judge_win_poker_player(["3C", "3D", "3S", "9S", "9D"])
        {6 : 3}
    Note:
        引数がlist()の場合の動作不明
    """
    hands_num, hands_suit = get_poker_hands_info(hands)

    role_dict = dict()
    card_max_num = 0
    # 複数の役に当てはまる手札があるため、強い役からチェックする
    for func_id in range(len(role_rank_func), 0, -1):
        # 関数をリストに入れているため、引数をそろえている（関数によっては未使用の引数がある）
        card_max_num = role_rank_func[func_id - 1](hands_num, hands_suit)
        if card_max_num != 0:
            role_dict[func_id - 1] = card_max_num
            break
    return role_dict


def get_poker_hands_info(hands: list) -> list:
    """
    引数(5枚の手札)からポーカーの役と役の中で最も大きいカードを返す
    Args:
        hands   (list)  :   プレイヤーの手札（数値 & マーク）
    Returns:
        hands_num   (list)  :   手札のカードの数値部分
        hands_suit  (list)  :   手札のカードのマーク部分
    Raises:
        不明    :   引数がlist()の場合に例外が発生する？
    Yields:
        -   :   無し
    Examples:
        >>> get_poker_hands_info(["5H", "5C", "6S", "7S", "KD"])
        [5, 5, 6, 7, 13], ["H", "C", "S", "S", "D"]
        >>> get_poker_hands_info(["2C", "3S", "8S", "8D", "TD"])
        [2, 3, 8, 8, 10], ["C", "S", "S", "D", "D"]
        >>> get_poker_hands_info(["5D", "8C", "9S", "JS", "AC"])
        [5, 8, 9, 11, 14], ["D", "C", "S", "S", "C"]
        >>> get_poker_hands_info(["2C", "5C", "7D", "8S", "QH"])
        [2, 5, 7, 8, 12], ["C", "C", "D", "S", "H"]
        >>> get_poker_hands_info(["2D", "9C", "AS", "AH", "AC"])
        [2, 9, 14, 14, 14], ["D", "C", "S", "H", "C"]
        >>> get_poker_hands_info(["3D", "6D", "7D", "TD", "QD"])
        [3, 6, 7, 10, 12], ["D", "D", "D", "D", "D"]
        >>> get_poker_hands_info(["4D", "6S", "9H", "QH", "QC"])
        [4, 6, 9, 12, 12], ["D", "S", "H", "H", "C"]
        >>> get_poker_hands_info(["3D", "6D", "7H", "QD", "QS"])
        [3, 6, 7, 12, 12], ["D", "D", "H", "D", "S"]
        >>> get_poker_hands_info(["2H", "2D", "4C", "4D", "4S"])
        [2, 2, 4, 4, 4], ["H", "D", "C", "D", "S"]
        >>> get_poker_hands_info(["3C", "3D", "3S", "9S", "9D"])
        [3, 3, 3, 9, 9], ["C", "D", "S", "S", "D"]
    Note:
        引数がlist()の場合の動作不明
        戻り値が複数の際のアノテーションの記載方法が不明
    """
    hands_num = list()
    hands_suit = list()
    for hand in hands:
        hands_num.append(cards_num_dict[hand[0]])
        hands_suit.append(hand[1])
    return hands_num, hands_suit


if __name__ == "__main__":
    print(problem_54())

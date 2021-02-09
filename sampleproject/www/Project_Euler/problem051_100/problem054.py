'''Project Euler Problem 54'''

# 訳注 : この問題に置いてA 2 3 4 5というストレートは考えなくてもよい
cards_num_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
                    '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

# 関数をリストとして保持したいため、対象関数をリストの前に記載する
def get_poker_hands_no_role(hands_num: list, hands_suit: list) -> int:
    '''
        ポーカーの役無し
        引数handsからポーカーの手札の中で最も大きいカードを返す
            return 最も大きい数字
    '''
    return max(hands_num)

def get_poker_hands_one_pair(hands_num: list, hands_suit: list) -> int:
    '''
        引数handsからポーカーのワンペアと役の中で最も大きいカードを返す
            return == 0 -> 役無し
            return != 0 -> 役有り、最も大きい数字はreturn値
    '''
    for num in hands_num:
        if hands_num.count(num) == 2:
            return num
    return 0

def get_poker_hands_two_pair(hands_num: list, hands_suit: list) -> int:
    '''
        引数handsからポーカーのツーペアと役の中で最も大きいカードを返す
            return == 0 -> 役無し
            return != 0 -> 役有り、最も大きい数字はreturn値
    '''
    one_pair_num = get_poker_hands_one_pair(hands_num, hands_suit)
    two_pair_num = get_poker_hands_one_pair(
                    list(filter(lambda x: x != one_pair_num, hands_num)), hands_suit)

    max_num = 0 if two_pair_num == 0 else max(one_pair_num, two_pair_num)
    return max_num

def get_poker_hands_three_cards(hands_num: list, hands_suit: list) -> int:
    '''
        引数handsからポーカーのスリーカードと役の中で最も大きいカードを返す
            return == 0 -> 役無し
            return != 0 -> 役有り、最も大きい数字はreturn値
    '''
    for num in hands_num:
        if hands_num.count(num) == 3:
            return num
    return 0

def get_poker_hands_strait(hands_num: list, hands_suit: list) -> int:
    '''
        引数handsからポーカーのストレートと役の中で最も大きいカードを返す
            return == 0 -> 役無し
            return != 0 -> 役有り、最も大きい数字はreturn値
        訳注 : この問題に置いてA 2 3 4 5というストレートは考えなくてもよい
    '''
    for i in range(len(hands_num)-1):
        if sorted(hands_num)[i]+1 != sorted(hands_num)[i+1]:
            return 0
    return max(hands_num)

def get_poker_hands_flash(hands_num: list, hands_suit: list) -> int:
    '''
        引数handsからポーカーのフラッシュと役の中で最も大きいカードを返す
            return == 0 -> 役無し
            return != 0 -> 役有り、最も大きい数字はreturn値
    '''
    if len(set(hands_suit)) == 1:
        return max(hands_num)
    return 0

def get_poker_hands_fullhouse(hands_num: list, hands_suit: list) -> int:
    '''
        引数handsからポーカーのフルハウスと役の中で最も大きいカードを返す
            return == 0 -> 役無し
            return != 0 -> 役有り、最も大きい数字はreturn値
    '''
    three_card_num = get_poker_hands_three_cards(hands_num, hands_suit)
    one_pair_num = get_poker_hands_one_pair(
                    list(filter(lambda x: x != three_card_num, hands_num)), hands_suit)

    max_num = 0 if one_pair_num == 0 or three_card_num == 0 else three_card_num
    return max_num

def get_poker_hands_four_cards(hands_num: list, hands_suit: list) -> int:
    '''
        引数handsからポーカーのフォーカードと役の中で最も大きいカードを返す
            return == 0 -> 役無し
            return != 0 -> 役有り、最も大きい数字はreturn値
    '''
    for num in hands_num:
        if hands_num.count(num) == 4:
            return num
    return 0

def get_poker_hands_strait_flash(hands_num: list, hands_suit: list) -> int:
    '''
        引数handsからポーカーのストレートフラッシュと役の中で最も大きいカードを返す
            return == 0 -> 役無し
            return != 0 -> 役有り、最も大きい数字はreturn値
        訳注 : この問題に置いてA 2 3 4 5というストレートは考えなくてもよい
    '''
    strait_num = get_poker_hands_strait(hands_num, hands_suit)
    flash_num = get_poker_hands_flash(hands_num, hands_suit)
    max_num = 0 if min(strait_num, flash_num) == 0 else max(strait_num, flash_num)
    return max_num

def get_poker_hands_royal_flash(hands_num: list, hands_suit: list) -> int:
    '''
        引数handsからポーカーのロイヤルフラッシュと役の中で最も大きいカードを返す
            return == 0 -> 役無し
            return != 0 -> 役有り、最も大きい数字はreturn値
        訳注 : この問題に置いてA 2 3 4 5というストレートは考えなくてもよい
    '''
    strait_num = get_poker_hands_strait_flash(hands_num, hands_suit)
    if strait_num == cards_num_dict['A']:
        return max(hands_num)
    return 0

role_rank_func = [get_poker_hands_no_role,
                    get_poker_hands_one_pair,
                    get_poker_hands_two_pair,
                    get_poker_hands_three_cards,
                    get_poker_hands_strait,
                    get_poker_hands_flash,
                    get_poker_hands_fullhouse,
                    get_poker_hands_four_cards,
                    get_poker_hands_strait_flash,
                    get_poker_hands_royal_flash]

def problem_54() -> int:
    '''Poker hands'''
    p_one_wins = 0
    with open('p054_poker.txt', 'rt') as file_p:
        read_lines = file_p.readlines()
    for cards in read_lines:
        if len(cards) < 2:
            continue
        player_one = cards[:len(cards)//2].split()
        player_two = cards[len(cards)//2:].split()
        if judge_win_poker_player(player_one, player_two):
            p_one_wins += 1
    return p_one_wins

def judge_win_poker_player(p_one: list, p_two: list) -> bool:
    '''
        引数p_oneと引数p_twoの手札でポーカーをし、引数p_oneの手札が勝つかどうか判断する
            True  -> 引数p_oneの手札が勝つ
            False -> 引数P_twoの手札が勝つ
    '''
    player_one_dict = get_poker_hands(p_one)
    player_two_dict = get_poker_hands(p_two)
    p_one_role = list(player_one_dict.keys())[0]
    p_two_role = list(player_two_dict.keys())[0]
    if p_one_role > p_two_role:
        return True
    if p_one_role == p_two_role:
        if player_one_dict[p_one_role] > player_two_dict[p_two_role]:
            return True
    return False

def get_poker_hands(hands: list) -> dict:
    '''
        5枚の手札(引数hands)からポーカーの役と役の中で最も大きいカードを返す
            ex) 引数handsの内部
                8C, TS, KC, 9H, 4S
    '''
    hands_num = list()
    hands_suit = list()
    for hand in hands:
        hands_num.append(cards_num_dict[hand[0]])
        hands_suit.append(hand[1])

    role_dict = dict()
    card_max_num = 0
    for func_id in range(len(role_rank_func), 0, -1):
        # 関数をリストに入れているため、引数をそろえた（未使用の引数がある）
        card_max_num = role_rank_func[func_id-1](hands_num, hands_suit)
        if card_max_num != 0:
            role_dict[func_id-1] = card_max_num
            break
    return role_dict

if __name__ == '__main__':
    print(problem_54())

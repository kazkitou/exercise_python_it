'''Project Euler Problem 28'''

def problem_28() -> int:
    '''Number spiral diagonals'''
    side_num = 1001
    return get_sum_diagonal(side_num)

def get_sum_diagonal(side_num: int) -> int:
    '''
        1から初めて右方向に進み時計回りに数字を増やしていき, 引数side_num × side_numの表に対する計算を行う。
        side_num × side_numの正方形上の対角線の和を返す。
            ex) side_num = 5
                return = 1 + 3 + 5 + 7 + 9 + 13 + 17 + 21 + 25
        右上に当たる値が引数side_num枠内の最大値となり、引数side_num**2になる。
        右上を起点にして、逆時計回りに算出可能。
            ex) side_num = 5
                右上    ＝  25 <- (5**2)
                左上    ＝  右上 - (side_num - 1)
                左下    ＝  左上 - (side_num - 1)
                右下    ＝  左下 - (side_num - 1)
    '''
    sum_diagonal = 0
    for i in range(side_num, 0, -2):
        sum_diagonal += get_sum_circumference(i)

    return sum_diagonal

def get_sum_circumference(side_num: int) -> int:
    '''
        外周の角にある値の合計を返す。
    '''
    if side_num < 1 or side_num % 2 == 0:
        # 正方形にならない引数side_numの場合は0
        return 0
    if side_num == 1:
        return 1
    right_up_num = side_num**2
    left_up_num = right_up_num - (side_num - 1)
    left_down_num = left_up_num - (side_num - 1)
    right_down_num = left_down_num - (side_num - 1)

    return right_up_num + left_up_num + left_down_num + right_down_num

if __name__ == '__main__':
    print(problem_28())

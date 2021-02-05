'''Project Euler Problem 39'''

def problem_39() -> int:
    '''Integer right triangles'''
    resolved_num = 0
    max_resolved_num = 0
    ret_p = 0
    for circumference in range(1000, 0, -1):
        resolved_num = get_right_angled_triangle_side(circumference)
        if max_resolved_num < resolved_num:
            max_resolved_num = resolved_num
            ret_p = circumference
    return ret_p

def get_right_angled_triangle_side(circumference) -> int:
    '''
        各辺の和が引数circumferenceの直角三角形の解の数を返す
            辺 a, b, c ... (c > b > a)
            a**2 + b**2 == c**2
    '''
    resolved_num = 0
    # a, b, cの3辺でaが一番小さい
    side_a_max = circumference//3+1
    for side_a in range(1, side_a_max):
        # b, cの2辺でbが一番小さい
        side_b_max = (circumference - side_a) // 2 + 1
        for side_b in range(side_a, side_b_max):
            # 外周と辺 a, b から辺 c を算出
            side_c = circumference - side_b - side_a
            if side_a**2 + side_b**2 == side_c**2:
                resolved_num += 1

    return resolved_num

if __name__ == '__main__':
    print(problem_39())

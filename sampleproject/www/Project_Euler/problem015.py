'''Project Euler Problem 15'''

def problem_15() -> int:
    '''Lattice paths'''
    # 20×20マスを最短ルート（後戻りなし）で端から端まで移動するパターン数を出す。
    # 縦20マス＋横20マス（＝40マス）を移動すると目的地に着く。
    # 後戻りなしのため、縦か横のどちらかの移動回数が限界まで来ると、もう片方は一意に決まる。
    # そのため全40マス移動中に20回（縦or横の限界マス移動数）移動するパターン数を出す。
    ret = combination((20+20), 20)
    return ret

def combination(num_m:int, num_n: int) -> int:
    '''
        mCn
            m * (m-1) * (m-2) * ... * (m-n)
            -------------------------------
            n * (n-1) * (n-2) * ... *   1
    '''
    if num_m < num_n:
        return 0

    tmp_m = 1
    tmp_n = 1
    tmp_cnt = 0
    for i in range(num_n, 0, -1):
        tmp_n *= i
        tmp_m *= (num_m - tmp_cnt)
        tmp_cnt += 1

    return tmp_m / tmp_n

if __name__ == '__main__':
    print(problem_15())

'''Project Euler Problem 31'''

def problem_31() -> int:
    '''Coin sums'''
    # 単純に全種類のコインの枚数分の繰り返し調査を行った。
    # pylintの指摘が多いため、よくない。再帰を用いて短くしたい。

    p1 = 1      # 1ペンス
    p2 = 2      # 2ペンス
    p5 = 5      # 5ペンス
    p10 = 10    # 10ペンス
    p20 = 20    # 20ペンス
    p50 = 50    # 50ペンス
    p100 = 100  # £1
    p200 = 200  # £2

    pattern_cnt = 0
    for i in range(0, p200+1, p100):
        if i >= p200:
            if i == p200:
                pattern_cnt += 1
            break
        for j in range(0, p200+1, p50):
            if (i + j) >= p200:
                if (i + j) == p200:
                    pattern_cnt += 1
                break
            for k in range(0, p200+1, p20):
                if (i + j + k) >= p200:
                    if (i + j + k) == p200:
                        pattern_cnt += 1
                    break
                for l in range(0, p200+1, p10):
                    if (i + j + k + l) >= p200:
                        if (i + j + k + l) == p200:
                            pattern_cnt += 1
                        break
                    for m in range(0, p200+1, p5):
                        if (i + j + k + l + m) >= p200:
                            if (i + j + k + l + m) == p200:
                                pattern_cnt += 1
                            break
                        for n in range(0, p200+1, p2):
                            if (i + j + k + l + m + n) >= p200:
                                if (i + j + k + l + m + n) == p200:
                                    pattern_cnt += 1
                                break
                            for o in range(0, p200+1, p1):
                                if (i + j + k + l + m + n + o) >= p200:
                                    pattern_cnt += 1
                                    break
    return pattern_cnt

def get_pattern_coins_sum(kind_coins: list, sum_limit: int) -> int:
    '''
        再帰関数
            引数kind_coinsの組み合わせで引数sum_limit以上となる組み合わせパターン数を返す
    '''

    if len(kind_coins) == 0:
        return 0

    pattern = 0
    # 値の大きなコインから繰り返したほうが処理回数が少なくなると考え、ソートする
    kind_coins.sort(reverse=True)
    step_num = kind_coins[0]
    for i in range(0, sum_limit+1, step_num):
        if i >= sum_limit:
            # 規定値を超えてからの繰り返しは無効と考える
            pattern += 1
            break
        pattern += get_pattern_coins_sum(kind_coins[1:len(kind_coins)], sum_limit - i)
    return pattern

if __name__ == '__main__':
    print(problem_31())
    print(\
        '''
        上記が正しい値だと思われるが、他回答を見ると£2を作るのに£2を用いているパターンも含んでいた。
        そのため続けて再帰処理を利用して、£2を用いて£2を作るパターンも含んだ数を求めた。
        以下がその結果となる。
        ''')
    print(get_pattern_coins_sum([1,2,5,10,20,50,100,200], 200))

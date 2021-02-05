'''Project Euler Problem 22'''

def problem_22() -> int:
    '''	Names scores'''
    # nameファイル読み出し
    read_name_txt = list()
    with open('names.txt', 'rt') as file_p:
        read_name_txt = file_p.read().split(',')
    read_name_txt.sort()

    # 辞書作成
    alphabet_rating = {}
    alpha_count = 1
    for alpha in range(ord('A'), ord('Z')+1):
        alphabet_rating[chr(alpha)] = alpha_count
        alpha_count += 1

    # Score
    all_score = 0
    count = 1
    for name in read_name_txt:
        score = 0
        for alp in name:
            if alp in alphabet_rating:
                # 'A'-'Z'以外は計測対象外とする
                score += alphabet_rating[alp]
        all_score += score * count
        count += 1

    return all_score

if __name__ == '__main__':
    print(problem_22())

"""Project Euler Problem 18"""


def problem_18() -> int:
    """Maximum path sum I"""
    max_rout_list_str = [
        "75",
        "95 64",
        "17 47 82",
        "18 35 87 10",
        "20 04 82 47 65",
        "19 01 23 75 03 34",
        "88 02 77 73 07 63 67",
        "99 65 04 28 06 16 70 92",
        "41 41 26 56 83 40 80 70 33",
        "41 48 72 33 47 32 37 16 94 29",
        "53 71 44 65 25 43 91 52 97 51 14",
        "70 11 33 28 77 73 17 78 39 68 17 57",
        "91 71 52 38 17 14 91 43 58 50 27 29 48",
        "63 66 04 68 89 53 67 30 73 16 69 87 40 31",
        "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23",
    ]
    # 全経路の数値（リスト）変換
    max_rout_list = []
    for num_list in max_rout_list_str:
        tmp_list = []
        for tmp_num in num_list.split():
            tmp_list.append(int(tmp_num))
        max_rout_list.append(tmp_list)

    # 下段から経路算出していく
    # 上段からは最適な経路を算出できない（過剰に加算される or 直近の数値で大きい和の方の比較加算しかできない）
    for row in range(len(max_rout_list) - 2, -1, -1):
        for column in range(len(max_rout_list[row])):
            big_data = 0
            if max_rout_list[row + 1][column] > max_rout_list[row + 1][column + 1]:
                big_data = max_rout_list[row + 1][column]
            else:
                big_data = max_rout_list[row + 1][column + 1]
            max_rout_list[row][column] += big_data

    return max_rout_list[0][0]


if __name__ == "__main__":
    print(problem_18())

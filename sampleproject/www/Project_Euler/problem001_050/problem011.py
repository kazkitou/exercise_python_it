"""Project Euler Problem 11"""


def problem_11() -> int:
    """Largest product in a grid"""
    input_str = []
    input_str.append("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08")
    input_str.append("49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00")
    input_str.append("81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65")
    input_str.append("52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91")
    input_str.append("22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80")
    input_str.append("24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50")
    input_str.append("32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70")
    input_str.append("67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21")
    input_str.append("24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72")
    input_str.append("21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95")
    input_str.append("78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92")
    input_str.append("16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57")
    input_str.append("86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58")
    input_str.append("19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40")
    input_str.append("04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66")
    input_str.append("88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69")
    input_str.append("04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36")
    input_str.append("20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16")
    input_str.append("20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54")
    input_str.append("01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")
    # 文字列を数値リストに入れ替える
    input_int = []
    for i in input_str:
        tmp = []
        for j in i.split():
            tmp.append(int(j))
        input_int.append(tmp)

    direction_max_val = []
    # 縦方向の調査
    direction_max_val.append(check_matrix_vertical(input_int))
    # 横方向の調査
    direction_max_val.append(check_matrix_side(input_int))
    # 斜め方向の調査
    direction_max_val.append(check_matrix_slant(input_int))

    return max(direction_max_val)


def check_matrix_vertical(ary: list) -> int:
    """20×20行列の縦方向計算"""
    max_val = 0
    for i in range(len(ary) - 4 + 1):
        # index = 0, 1, 2, ..., 15, "16", 17, 18, 19
        for j in range(len(ary[i])):
            # index = 0, 1, 2, ..., 15, 16, 17, 18, "19"
            tmp = 1
            for k in range(4):
                tmp *= ary[i + k][j]
            if tmp > max_val:
                max_val = tmp
    return max_val


def check_matrix_side(ary: list) -> int:
    """20×20行列の横方向計算"""
    max_val = 0
    # pylintに len(ary) 部分が指摘されるため len(ary)+0 にした。
    # 可変する変数がダメなようなので、リストではなくタプルにするのが無難と思われる。
    for i in range(len(ary) + 0):
        # index = 0, 1, 2, ..., 15, 16, 17, 18, "19"
        for j in range(len(ary[i]) - 4 + 1):
            # index = 0, 1, 2, ..., 15, 16, 17, 18, 19
            tmp = 1
            for k in range(4):
                tmp *= ary[i][j + k]
            if tmp > max_val:
                max_val = tmp
    return max_val


def check_matrix_slant(ary: list) -> int:
    """20×20行列の斜め方向（右下、左下の両方）計算"""
    max_val = 0
    # 斜め方向（右下）計算
    for i in range(len(ary) - 4 + 1):
        # index = 0, 1, 2, ..., 15, "16", 17, 18, 19
        for j in range(len(ary[i])):
            # index = 0, 1, 2, ..., 15, 16, 17, 18, "19"
            tmp = 1
            for k in range(4):
                if (j + k) >= len(ary[i]):
                    tmp = 1
                    break
                tmp *= ary[i + k][j + k]
            if tmp > max_val:
                max_val = tmp

    # 斜め方向（左下）計算
    for i in range(len(ary) - 4 + 1):
        # index = 0, 1, 2, "3", ..., 15, 16, 17, 18, 19
        for j in range(len(ary[i]) - 1, -1, -1):
            # index = "0", 1, 2, 3, ..., 15, 16, 17, 18, 19
            tmp = 1
            for k in range(4):
                if (j - k) < 0:
                    tmp = 1
                    break
                tmp *= ary[i + k][j - k]
            if tmp > max_val:
                max_val = tmp

    return max_val


if __name__ == "__main__":
    print(problem_11())

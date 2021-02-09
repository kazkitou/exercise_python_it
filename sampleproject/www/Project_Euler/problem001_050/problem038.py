"""Project Euler Problem 38"""


def problem_38() -> int:
    """Pandigital multiples"""
    # 積がパンデジタル数のものを求めるため、積が9桁を超えることはない。
    # 整数 × (1, 2, ...  , n)　(n > 1) = 9桁以下
    # Pattern1     abcdefghi × 1 = 9桁 ... n > 1の条件に当てはまらないのでNG
    # Pattern2     abcde     × 1 = 5桁
    #              abcde     × 2 = 5桁 ... 積が9桁を超えるのでNG
    # Pattern3     abcd      × 1 = 4桁
    #              abcd      × 2 = 5桁 ... これが最大の整数(4桁)
    max_pandigital = 0
    for left_num in range(1, 10000):
        combination_num = 0
        right_num = 1
        while len(str(combination_num)) < 9:
            combination_num = int(str(combination_num) + str(left_num * right_num))
            right_num += 1
        if sorted(str(combination_num)) == list("123456789"):
            if max_pandigital < combination_num:
                max_pandigital = combination_num
    return max_pandigital


if __name__ == "__main__":
    print(problem_38())

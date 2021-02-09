"""Project Euler Problem 42"""
import itertools


def problem_42() -> int:
    """Coded triangle numbers"""
    tri_num_cnt = 0
    with open("p042_words.txt", "rt", encoding="utf-8") as file_open:
        read_txt = file_open.read()
    read_txt_list = read_txt.split(",")
    for read_line in read_txt_list:
        read_line = read_line.replace('"', "")
        read_line = read_line.rstrip("\n")
        check_num = 0
        for charactor in read_line.lower():
            check_num += "abcdefghijklmnopqrstuvwxyz".find(charactor) + 1
        if judge_triangular_number(check_num):
            tri_num_cnt += 1
    return tri_num_cnt


def judge_triangular_number(num: int) -> bool:
    """
    引数num項が三角数であるか判断する
        True  -> 三角数である
        False -> 三角数でない
    """
    check_num = 0
    for i in itertools.count(1):
        check_num = get_triangular_number(i)
        if num == check_num:
            return True
        if check_num > num:
            break
    return False


def get_triangular_number(term: int) -> int:
    """
    引数term項にあたる三角数を返す
    三角数とは多角数の一種で、正三角形の形に点を並べたときにそこに並ぶ点の総数のことである。
    n番目の三角数は 1 から n までの自然数の和に等しい。
        1 + 2 + 3 + ... + n = n(n+1)/2
    """
    if term < 1:
        return 0
    return (term * (term + 1)) / 2


if __name__ == "__main__":
    print(problem_42())

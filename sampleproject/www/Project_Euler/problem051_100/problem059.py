"""Project Euler Problem 59"""
import itertools
import math


def problem_59() -> int:
    """XOR decryption"""
    read_data = ""
    with open("p059_cipher.txt", "rt") as file_p:
        read_data = file_p.read().split()
        print(read_data)
    return -1


if __name__ == "__main__":
    print(problem_59())

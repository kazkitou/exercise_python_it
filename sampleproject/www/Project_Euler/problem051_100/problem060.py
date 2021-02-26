"""Project Euler Problem 60 module"""
import itertools

class problem_060:
    """Project Euler Problem 60 class"""
    def __init__(self) -> None:
        """Prime pair sets"""
        self.five_prime_set_sum_minimum = 0
        self.prim_set = list()

    def resolved_problem(self) -> int:
        min_sum = 0
        check_prim_list = list()
        for i in itertools.count(2):
            if self.is_prim_decision(i):
                check_prim_list.append(i)
                if len(check_prim_list) < 4:
                    continue
                comb_num = 4
                for check_list in itertools.permutations(check_prim_list, comb_num):
                    if self.is_quite_remarkable_prim_number_combination(check_list):
                        if min_sum == 0 or sum(check_list) < min_sum:
                            min_sum = sum(check_list)
                    else:
                        min_sum = 0
                        continue
            if min_sum != 0:
                break
        return min_sum

    def is_prim_decision(self, num: int) -> bool:
        """{num}の素数判定"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    def is_quite_remarkable_prim_number_combination(self, prim_num_list: list) -> bool:
        """{prim_num_list}内の2つの組み合わせが全て素数か確認する"""
        for comb in itertools.permutations(prim_num_list, 2):
            check_num = int("".join(map(str, comb)))
            if not self.is_prim_decision(check_num):
                return False
        return True

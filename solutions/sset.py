# Given a positive intenger n <= 1000, find the number of subsets of the set {1, 2, ..., n}
# modulo 1000000

from itertools import combinations

def subsets(n: int) -> int:
    num = 1
    for i in range(1, n + 1):
        num *= 2
        if num > 1000000:
            num %= 1000000
        elif num == 1000000:
            return 0
    return num

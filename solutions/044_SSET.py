# Given a positive intenger n <= 1000, find the number of 
# subsets of the set {1, 2, ..., n} modulo 1000000

# For every item in the set, the item can either be in the subset or not
# This means that there are 2^n possible subsets for a set of length n
def subsets(n: int) -> int:
    num = 1
    for i in range(1, n + 1):
        num *= 2
        if num > 1000000:        # If the remainder is at any point 0, then the answer is 0
            num %= 1000000
        elif num == 1000000:
            return 0
    return num

# Find the number of partial permutations mod 10^6
# Computes nPk with factorials


def partialPerms(n: int, k: int) -> int:
    num = 1
    for i in range(n-k+1, n+1):
        num *= i
        if num > 1000000:
            num %= 1000000
        elif num == 1000000:
            return 0
    return num

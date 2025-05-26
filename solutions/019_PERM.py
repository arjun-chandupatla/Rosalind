from itertools import permutations


def getPerms(n: int):
    l = list(permutations(range(1, n+1)))
    return (len(l), l)


def formatOutput(l: int, p: list[tuple]) -> str:
    s = str(l)
    for i in p:
        s += "\n"
        for j in i:
            s += str(j) + " "
    return s

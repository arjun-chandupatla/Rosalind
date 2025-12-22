# given an rna strand, find the number of maximum matchings



def maximumMatchings(rna: str) -> int:
    a = 0
    c = 0
    g = 0
    u = 0
    for base in rna:
        if base == "A":
            a += 1
        elif base == "C":
            c += 1
        elif base == "G":
            g += 1
        elif base == "U":
            u += 1

    auMatchings = perm(max(a, u), min(a, u))
    gcMatchings = perm(max(g, c), min(g, c))
    return auMatchings*gcMatchings


def parseInput(file):
    text = file.read()
    print(text)
    return ("GUCGGGAAGUGUUGCACUUGUACCAUUAUCUGAUCCCAUCCCCUCAACUUCAUAGUGCGACCUCACAGACGUGCAGAUUCCAGUCCCUUCGA")


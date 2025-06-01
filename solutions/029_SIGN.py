# Given a number n <= 6, return all the possible signed permutations of length n
# A signed permutation is a permutation, but every number is prefaced with either 
# a positive or a negative sign

from itertools import permutations

def getPerms(n: int):    # Generates and returns list of signed permutations
    alph = list(range(1, n+1))
    l = len(alph)
    for i in range(l):
        term = alph[i]
        alph.append(-term)

    perms = list(permutations(alph, n))
    for j in range(len(perms) - 1, -1, -1):
        item = list(perms[j])
        temp = list(map(abs, item))
        if len(temp) != len(set(temp)):
            del perms[j]
        
    return perms


def formatOutput(perms: list) -> str:    # Formats the output for the rosalind autograder
    s = str(len(perms))
    for p in perms:
        s += "\n"
        temp = ""
        for q in p:
            temp += str(q) + " "
        s += temp.strip()
    return s

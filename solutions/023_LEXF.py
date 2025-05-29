# List all k-mers alphabetically provided an alphabet and a length
# Computes the Cartesian product of the alphabet set with itertools

from itertools import product

def allKmers(alphabet: list[str], n: int):
    return list(product(alphabet, repeat=n))


def formatOutput(ans) -> str:
    s = ""
    for i in ans:
        for j in i:
            s += j
        s += "\n"
    return s

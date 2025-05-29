# List all k-mers alphabetically provided an alphabet and a length
# Computes the Cartesian product of the alphabet set with itertools

from itertools import product


# Computes the list of kmers
# This list is sorted if alphabet is sorted
def allKmers(alphabet: list[str], n: int):
    return list(product(alphabet, repeat=n))


# Format the list into a string for Rosalind
def formatOutput(ans) -> str:
    s = ""
    for i in ans:
        for j in i:
            s += j
        s += "\n"
    return s

# Given a DNA string s, find the 4-mer composition of s

# A kmer is a string of length k, in this case being a DNA string of length k
# The kmer composition of a string is the number of times each possible kmer appears in it
# in order alphabetically

import itertools

# Generate all possible kmers
def getKmers(k: int):
    temp = list(itertools.product(["A", "C", "G", "T"], repeat=k))
    kmers = [""] * len(temp)
    for i in range(len(temp)):
        kmers[i] = "".join(temp[i])
    return kmers

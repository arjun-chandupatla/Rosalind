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


# Find kmer composition of a string
def composition(dna: str) -> list[int]:
    kmers = getKmers()
    kmer_map = dict()
    comp = [0] * len(kmers)
    for i in range(len(kmers)):
        kmer_map[kmers[i]] = i
        print(kmer_map)
    for j in range(len(dna) - 3):
        kmer = dna[j:j+4]
        idx = kmer_map[kmer]
        comp[idx] += 1
    return comp

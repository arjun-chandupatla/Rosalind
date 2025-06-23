# Given a DNA string s, find the 4-mer composition of s

# A kmer is a string of length k, in this case being a DNA string of length k
# The kmer composition of a string is the number of times each possible kmer appears in it
# in order alphabetically



# Generate all possible 4-mers
def getKmers():
    temp = list(itertools.product(["A", "C", "G", "T"], repeat=4))
    kmers = [""] * len(temp)
    for i in range(len(temp)):
        kmers[i] = "".join(temp[i])
    return kmers

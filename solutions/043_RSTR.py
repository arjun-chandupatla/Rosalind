# Determine the probability that a certain motif would occur in a random genome
# It is simpler to find the probability that the motif wouldn't occur, and then
# find the complement of that probability


# N is the number of randomly constructed strings, the GC content of the genome,
# and a motif of under 10 base pairs
def getProb(N: int, gc: float, motif: str):
    AT, GC = 0, 0     
    for base in motif:
        match base:
            case "A" | "T":
                AT += 1
            case "G" | "C":
                GC += 1
    # Find the probability of the motif not occurring in one random strand
    p = ((0.5 * gc)**GC) * ((0.5 * (1 - gc))**AT)
    return 1 - (1-p)**N

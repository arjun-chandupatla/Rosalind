# Determine the probability that a certain motif would occur in a random genome
# It is simpler to find the probability that the motif wouldn't occur, and then
# find the complement of that probability
def getProb(n: int, gc: float, motif: str):
    AT, GC = 0, 0     
    for base in motif:
        match base:
            case "A" | "T":
                AT += 1
            case "G" | "C":
                GC += 1
    p = ((0.5 * gc)**GC) * ((0.5 * (1 - gc))**AT)
    return 1 - (1-p)**n

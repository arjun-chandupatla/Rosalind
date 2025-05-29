# Basically finds the probability that a motif will occur through random chance in 
# a DNA sequence given its GC content
# Takes the log base 10 of each probability, so higher numbers (less negative) mean
# a higher probability
from math import log10

def probRandomString(s: str, gc_arr: list[float]):
    for gc in gc_arr:
        g = gc/2         # Probability of G or C
        a = (1-gc)/2     # Probability of A or T
        prob = 1.0
        for base in s:
            match base:
                case "A" | "T":
                    prob *= a
                case "C" | "G":
                    prob *= g
        yield log10(prob)

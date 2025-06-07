# random string matching

import numpy as np
def getProb(n: int, gc: float, motif: str):
    AT, GC = 0, 0     
    for base in motif:
        if base == "A":
            AT += 1
        elif base == "T":
            AT += 1
        elif base == "C":
            GC += 1
        elif base == "G":
            GC += 1
    p = ((0.5 * gc)**GC) * ((0.5 * (1 - gc))**AT)
    return 1 - (1-p)**n

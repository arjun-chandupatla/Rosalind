# random string matching

import numpy as np

def getProb(n: int, gc: float, motif: str):
    AT, GC = 0, 0     
    for base in motif:
        if base == "A" or base == "T":
            AT += 1
        elif base == "C" or base == "G":
            
    p = ((0.5 * gc)**GC) * ((0.5 * (1 - gc))**AT)
    return 1 - (1-p)**n

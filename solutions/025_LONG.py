# Simple attempt at chromosome reconstruction
# Provides a set of DNA strands, and assumes that the chromosome
# is the shortest superstring of the DNA set


# Finds the length of overlap between two strings
def overlap(s: str, t: str) -> int:
    if s == t:
        return len(s)
    o = -1      # Maximum overlap
    for i in range(1, min(len(s), len(t))):
        if s[-i:] == t[:i]:
            o = i
    return o


def getOrder(dna: list[str]):
    order = dict()
    for i in range(len(dna)):
        d1 = dna[i]
        overlap_arr = [0] * len(dna)
        for j in range(len(dna)):
            if i == j: continue
            d2 = dna[j]
            overlap_arr[j] = overlap(d1, d2)
        idx = overlap_arr.index(max(overlap_arr))
        order[d1] = dna[idx]
    
    l = []
    for k in order.keys():
        if k not in order.values():
            l = [k]
            break

    for _ in range(1, len(dna)):
        l.append(order[l[-1]])

    return l

# Return the "difference" in two strings
# Difference is measured by number of mismatches
# Counts point mutations

def hamming_distance(p: str, q: str) -> int:
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist

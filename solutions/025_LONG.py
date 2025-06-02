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

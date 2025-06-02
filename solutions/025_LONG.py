# Reconstruct a chromosome by assuming parsimony
# Essentially finds the shortest superstring given a set of strings


# Finds the length of overlap between two strings
def overlap(s: str, t: str) -> int:
    if s == t:
        return len(s)
    o = -1      # Maximum overlap
    for i in range(1, min(len(s), len(t))):
        if s[-i:] == t[:i]:
            o = i
    return o


# Finds and returns the order in which the strings should be joined
def getOrder(dna: list[str]):
    order = dict()      # order is a directed graph
    for i in range(len(dna)):
        d1 = dna[i]
        overlap_arr = [0] * len(dna)
        for j in range(len(dna)):
            if i == j: continue
            d2 = dna[j]
            overlap_arr[j] = overlap(d1, d2)
        idx = overlap_arr.index(max(overlap_arr))
        order[d1] = dna[idx]
    
    # Finds the only path (l) in a directed graph (order)
    l = []
    for k in order.keys():
        if k not in order.values():     # Finds the node with indegree 0
            l = [k]
            break
    # If there are n strings in dna, then the number of edges is (n-1)
    # so l is grown (n-1) times
    for _ in range(1, len(dna)):
        l.append(order[l[-1]])

    return l


# Creates the superstring given a list of strings in order
def superstring(dna_arr: list[str]):
    super = dna_arr[0]
    for i in range(1, len(dna_arr)):
        overlap_ = overlap(super, dna_arr[i])
        super += dna_arr[i][overlap_:]
    return super


def parseInput(file):
    temp = ""
    dna_arr = []
    for line_s in file:
        line = line_s.strip()
        if line.startswith(">"):
            dna_arr.append(temp)
            temp = ""
        else:
            temp += line
    dna_arr.append(temp)
    return dna_arr[1:]

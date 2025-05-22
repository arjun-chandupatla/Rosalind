# Create an overlap graph O_3 given a series of DNA strands in FASTA format

# Creates the overlap graph as a hashmap with the initial strand as a key and the following strand as a value
def overlapGraph(inp: dict[str, str], k: int) -> dict[str, list[str]]:
    pattern_set = dict()

    for p in inp.keys():
        kmer = inp[p]
        for q in inp.keys():
            kmer1 = inp[q]
            if kmer == kmer1:
                continue
            elif suffix(kmer, k) == prefix(kmer1, k):
                if p not in pattern_set.keys():
                    pattern_set[p] = []
                if q not in pattern_set[p]:
                    pattern_set[p].append(q)
    return pattern_set


# Returns the first k elements of a string
def prefix(kmer: str, k: int) -> str:
    return kmer[:k]


# Returns the last k elements of a string
def suffix(kmer: str, k: int) -> str:
    return kmer[-k:]


# Converts the FASTA form input, in a text file, to a hashmap
# overlapGraph reads the hashmap and creates the graph based on that
def parseInput(file):
    d = dict()
    temp = ""
    for line_s in file:
        line = line_s.strip()
        if line.isspace():
            continue
        elif line.startswith(">"):
            temp = line
            d[temp] = ""
        else:
            d[temp] += line.strip()
    return d


# Creates a Rosalind-friendly string output
def formatOutput(ans: dict[str, list[str]]) -> str:
    s = ""
    for k in ans.keys():
        for v in ans[k]:
            s += (k[1:] + " " + v[1:] + "\n")
    return s

# Given a list of reads, return which ones have a single-nucleotide replacement mutation

# Reverse complement
def rc(dna: str) -> str:
    s = ""
    for base in dna:
        match base:
            case "A":
                s += "T"
            case "C":
                s += "G"
            case "G":
                s += "C"
            case "T":
                s += "A"
    return s[::-1]


# Hamming Distance
def hd(p: str, q: str) -> int:
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist


# Find all the correct reads (will appear >=2 times)
def correctList(reads: list[str]):
    correct = []
    for i in range(len(reads)):
        r = reads[i]
        if r not in correct:
            if r in reads[i+1:] or rc(r) in reads[i+1:]:
                correct.append(r)
                #correct.append(rc(r))
        elif rc(r) in correct:
            correct.append(r)
    return correct


# Link the incorrect reads to their closest correct read
def errors(reads: list[str], correct: list[str]):
    map = {}
    for j in range(len(reads)):
        r = reads[j]
        if r not in correct or rc(r) not in correct:
            for k in range(len(correct)):
                if hd(r, correct[k]) == 1:
                    map[r] = correct[k]
                elif hd(r, rc(correct[k])) == 1:
                    map[r] = rc(correct[k])
    return map


# Format output for the Rosalind autograder
def formatOutput(map: dict[str, str]) -> str:
    s = ""
    for k in map.keys():
        s += k + "->" + map[k] + "\n"
    return s.rstrip()


# Parse the input (FASTA format)
def parseInput(inp: list[str]):
    temp = []
    for i in range(1, len(inp), 2):
        temp.append(inp[i].strip())
    return temp


if __name__ == "__main__":
    f = open("input.txt", "r")
    l = []
    for line in f:
        l.append(line)
    f.close()

    lines = parseInput(l)

    cor = correctList(lines)
    map = errors(lines, cor)
    ans = formatOutput(map)

    g = open("output.txt", "w")
    g.write(ans)
    g.close()

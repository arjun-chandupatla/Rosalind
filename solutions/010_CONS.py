# Create a consensus strand and a profile matrix
# for a set of DNA strands provided

from numpy import transpose

# Create the profile matrix
def profile(motifs):
    tMotifs = []
    for column in transpose(motifs):
        tMotifs.append(list(column))
    k = len(tMotifs[0])
    A = [0] * k
    C = [0] * k
    G = [0] * k
    T = [0] * k
    for i in range(k):
        for r in tMotifs:
            if r[i] == "A":
                A[i] += 1
            elif r[i] == "C":
                C[i] += 1
            elif r[i] == "G":
                G[i] += 1
            elif r[i] == "T":
                T[i] += 1
    return [A, C, G, T]


# Create the consensus strand from the profile matrix
def consensus(profile_arr):
    cons = ""
    prof = transpose(profile_arr)
    for i in prof:
        m = list(i).index(max(i))
        match m:
            case 0:
                cons += "A"
            case 1:
                cons += "C"
            case 2:
                cons += "G"
            case 3:
                cons += "T"
    return cons


# Format the consensus string and profile array for rosalind's autograder
def formatOutput(cons: str, prof: list[list[int]]) -> str:
    s = ""
    s += cons
    nuc = "ACGT"
    for r in range(4):
        temp = []
        s += "\n"
        s += nuc[r] + ": "
        for i in prof[r]:
            temp.append(str(i))
        s += " ".join(temp)
    return s


# Turn the input (a text file in FASTA format) into a list of DNA strands
# that profile() can use
def parseInput(file):
    d = list()
    temp = ""
    for line_s in file:
        line = line_s.strip()
        if line.isspace():
            continue
        elif line.startswith(">"):
            if len(temp) == 0:
                pass
            else:
                d.append(temp)
                temp = ""
        else:
            temp += line.strip()
    d.append(temp)
    return d

# Create a consensus strand and a profile matrix
# for a set of DNA strands provided

# Create the profile matrix
def count(motifs):
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
def consensus(count_arr):
    cons = ""
    c_arr = transpose(count_arr)
    for i in c_arr:
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

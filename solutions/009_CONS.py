# Create a consensus array


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

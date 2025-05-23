# Find the longest common substring of a set of DNA strings
# This substring is most likely a motif, and its function can be analyzed further

def parseInput(file) -> list[str]:
    dna = list()
    temp = ""
    for line_s in file:
        line = line_s.strip()
        if line.isspace():
            continue
        elif line.startswith(">"):
            if len(temp) == 0:
                pass
            else:
                dna.append(temp)
                temp = ""
        else:
            temp += line.strip()
    dna.append(temp)
    return dna


def findMotifs(dna_arr: list[str]) -> list[str]:
    motifs = []
    new_motifs = [""]
    while len(new_motifs) != 0:
        motifs = new_motifs
        new_motifs = []
        for m in motifs:		# regenerate new_motifs
            new_motifs += list(expand(m))
        for d in dna_arr:
            for i in range(len(new_motifs) - 1, -1, -1):
                if new_motifs[i] not in d:
                    del new_motifs[i]
    return motifs

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

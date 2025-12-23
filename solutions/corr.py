#error correction in reads


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


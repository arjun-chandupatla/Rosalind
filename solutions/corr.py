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


def hd(p: str, q: str) -> int:
    dist = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            dist += 1
    return dist


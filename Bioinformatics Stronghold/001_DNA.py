def count(path: str) -> tuple((str, str, str, str)): # type: ignore
    f = open(path, "r")
    dna = f.read()
    f.close()
    A, C, G, T = 0, 0, 0, 0
    for base in dna:
        match base:
            case "A": A += 1
            case "C": C += 1
            case "G": G += 1
            case "T": T += 1
    return (A, C, G, T)

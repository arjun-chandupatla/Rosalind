def reverse_complement(path: str) -> str:
    f = open(path, "r")
    template = f.read()
    f.close()
    rc = ""
    for base in template:
        match base:
            case "A": rc += "T"
            case "T": rc += "A"
            case "C": rc += "G"
            case "G": rc += "C"
    return rc[::-1]

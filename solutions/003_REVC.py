# Takes the reverse complement of a template DNA strand
# This is the sequence of the complementary strand read 5' to 3'

def reverse_complement(template: str) -> str:
    rc = ""
    for base in template:
        match base:
            case "A": rc += "T"
            case "T": rc += "A"
            case "C": rc += "G"
            case "G": rc += "C"
    return rc[::-1]

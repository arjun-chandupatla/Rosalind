# Output all the possible proteins that a strand of DNA could
# encode for. These start with the start codon and end with the
# stop codon in both the forward strand and its complement.

# RNA codon to amino acid hashmap
gen_code = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}


# All the possible proteins in one reading frame
def translateOpenReadingFrame(dna: str):
    global gen_code
    k = 3
    rna = dna.replace("T", "U")
    proteins = []

    for i in range(len(rna) + 1):
        codon = rna[i:i+k]
        if codon == "AUG":
            prot = ""
            for j in range(i, len(rna) + 1, 3):
                codon = rna[j:j+k]
                if len(codon) != 3:
                    break
                aa = gen_code[codon]
                if aa == "STOP":
                    proteins.append(prot)
                    break
                else:
                    prot += aa
    return proteins


# Finds the complementary strand
def reverseComplement(dna: str):
    rc = ""
    for base in dna:
        match base:
            case "A":
                rc += "T"
            case "T":
                rc += "A"
            case "C":
                rc += "G"
            case "G":
                rc += "C"
    return rc[::-1]


def parseInput(file):
    dna = ""
    for line_s in file:
        line = line_s.strip()
        if line.startswith(">"):
            pass
        elif line.isspace():
            pass
        else:
            dna += line
    return dna


def formatOutput(proteins):
    s = ""
    for p in list(set(proteins)):
        s += p + "\n"
    return s

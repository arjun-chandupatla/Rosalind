# Translates a strand of RNA
# Does not necessarily start at start codon here
def translate(rna: str) -> str:
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
    protein = ""
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        if gen_code[codon] == "STOP":
            return protein
        protein += gen_code[codon]


# Not the same as transcription
# RNA strand is not complementary
def dnaToRna(dna: str) -> str:
    return dna.replace("T", "U")


# Returns the coding regions of DNA
# Effectively splices introns out
def splice(dna, introns) -> str:
    splc_dna = dna
    for intron in introns:
        i = splc_dna.index(intron)
        l = len(intron)
        if splc_dna[i:i+l+1] == intron:
            raise IndexError("intron not same as splc_dna, index error")
        splc_dna = splc_dna[:i] + splc_dna[i+l:]
    return splc_dna

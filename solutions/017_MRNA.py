# Given a peptide, return the number of possible mRNA strands that could encode that peptide modulo 1,000,000

# Number of codons per peptide
num_pep = {"F":2, "L":6, "S":6, "Y":2, "C":2, "W":1, 
           "P":4, "H":2, "Q":2, "R":6, "I":3, "M":1, 
           "T":4, "N":2, "K":2, "V":4, "A":4, "D":2, 
           "G":4, "E":2}

def numMRNA(pep: str) -> int:
    global num_pep
    num = 1
    for aa in pep:
        if aa.isspace():
            pass
        else:
            num *= num_pep[aa]
            if num > 1000000:
                num %= 1000000
                if num == 0:
                    return 0
    num *= 3        # 3 different stop codon possibilities
    return num % 1000000

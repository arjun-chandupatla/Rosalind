# Find restriction sites in a strand of DNA. Restriction sites are 
# typically reverse palindromes, meaning that they are the same as 
# their reverse complement.


def reverseComplement(dna: str) -> str:
    rc = ""
    for base in dna:
        match base:
            case "A":
                rc += "T"
            case "C":
                rc += "G"
            case "G":
                rc += "C"
            case "T":
                rc += "A"
    return rc[::-1]

# Uses dict[int, list[int]] in order to account for the possibility
# of multiple restriction sites of different lengths starting 
# from the same index
def findRestrictionSites(dna: str) -> dict[int, list[int]]:
    site_arr = dict()
    for n in range(4, 13, 2):
        for i in range(len(dna) - n + 1):
            win = dna[i:i+n]
            if win == reverseComplement(win):
                if (i+1) not in site_arr.keys():
                    site_arr[i+1] = []
                site_arr[i+1].append(n)
    for k in site_arr.keys():
        site_arr[k].sort()
    return site_arr


def parseInput(file) -> str:
    dna = ""
    for line_s in file:
        line = line_s.strip()
        if line.startswith(">"):
            pass
        else:
            dna += line
    return dna


def formatOutput(sites: dict[int, list[int]]) -> str:
    s = ""
    site_k = list(sites.keys())
    site_k.sort()
    for k in site_k:
        for v in sites[k]:
            s += str(k) + " " + str(v) + "\n"

    return s

# FASTA file format parser
# Used to parse the input format for 005_GC on Rosalind

def parseFasta(path):
    f = open(path, "r")
    id = None
    d = dict()
    while True:
        line = f.readline()
        line = line.rstrip()
        if not line:
            f.close()
            return d
        if line.startswith(">"):
            id = line
            d[id] = """"""
        else:
            d[id] += line

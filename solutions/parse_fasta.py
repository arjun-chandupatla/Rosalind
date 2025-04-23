# FASTA file format parser

def parse_fasta(path):
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

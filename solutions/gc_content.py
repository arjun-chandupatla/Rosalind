# find GC-content of a DNA string
# DNA provided in FASTA format
# uses parse_fasta.py

from parse_fasta import *

def gc_content(dna_dict: dict[str: str]) -> tuple((str, float)): # type: ignore
    gc_dict = dict()
    for k in dna_dict.keys():
        dna = dna_dict[k]
        gc = 0
        for base in dna.lower():
            if base == "g" or base == "c":
                gc += 1
        gc_dict[k] = float(gc)/len(dna) * 100
    
    max_gc = max(gc_dict.values())
    for k in gc_dict.keys():
        if gc_dict[k] == max_gc:
            return (k, gc_dict[k])


if __name__ == "__main__":
    path = ""               # insert path
    dna_dict = parse_fasta(path)
    print(gc_content(dna_dict))

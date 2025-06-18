# Given a list of strings, return the one with the highest GC content

def gc_content(dna_dict: dict[str: str]) -> tuple((str, float)):
    gc_dict = dict()
    for k in dna_dict.keys():
        dna = dna_dict[k]
        gc = 0
        for base in dna:
            match base:
                case "G" | "C":
                    gc += 1
        gc_dict[k] = float(gc)/len(dna) * 100
    
    max_gc = max(gc_dict.values())
    for k in gc_dict.keys():
        if gc_dict[k] == max_gc:
            return (k, gc_dict[k])

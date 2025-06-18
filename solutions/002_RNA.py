# Transcribes a DNA strand into an RNA strand
# Does not take into account complements

def transcribe(path):
    f = open(path, "r")
    dna = f.read()
    f.close()
    rna = dna.replace("T", "U")
    return rna

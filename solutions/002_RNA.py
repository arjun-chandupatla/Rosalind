# Transcribes a DNA strand into an RNA strand
# Does not take into account complements

def transcribe(dna: str): -> str
    rna = dna.replace("T", "U")
    return rna

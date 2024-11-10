def transcribe(path):
    f = open(path, "r")
    dna = f.read()
    f.close()
    rna = dna.replace("T", "U")
    return rna



if __name__ == "__main__":
    path = ""   # insert path
    print(transcribe(path))

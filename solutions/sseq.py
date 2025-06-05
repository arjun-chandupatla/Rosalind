# find the indices of a subsequence the subsequence doesn't have to occur contiguously
# this reflects how motifs/genes aren't always contiguous, as well as the splicing process


def findIndices(dna: str, seq: str) -> list[int]:
    index_arr = [0]

    for base in seq:
        index_arr.append(dna.index(base, index_arr[-1]) + 1)

        
    return index_arr[1:]



def parseFasta(file):
    temp = ""
    arr  = []

    
    for line_s in file:
        line = line_s.strip()

        
        if line.startswith(">"):
            arr.append(temp)
            temp = ""
        else:
            temp += line
    
    
    arr.append(temp)
    
    return arr[1:]

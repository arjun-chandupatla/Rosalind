# find the indices of a subsequence the subsequence doesn't have to occur contiguously
# this reflects how motifs/genes aren't always contiguous, as well as the splicing process


def findIndices(dna: str, seq: str) -> list[int]:
    index_arr = [0]

    for base in seq:
        index_arr.append(dna.index(base, index_arr[-1]) + 1)

        
    return index_arr[1:]


def prob(n: int, seq: str, gc_arr: list[float]):
    for gc in gc_arr:
        p = 1
        for base in seq:
            if base == "A" or base == "T":
                p *= (1-gc)/2
            elif base == "C" or base == "G":
                p *= gc/2
        p *= n-len(seq)+1
        yield p

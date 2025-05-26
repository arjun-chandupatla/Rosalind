def perfectMatchings(rna: str) -> int:
    au = 0
    gc = 0
    for base in rna:        # Given that same number of A and U, and G and C
        if base == "A":
            au += 1
        elif base == "G":
            gc += 1
    return f(au) * f(gc)

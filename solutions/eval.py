from math import log10

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


i = open("input.txt", "r")
lines = i.readlines()
i.close()

n = int(lines[0].strip())
seq = lines[1].strip()
arr = list(map(float, lines[2].strip().split()))

ans = ""
for p in prob(n, seq, arr):
    ans += (str(p) + " ")


h = open("output.txt", "w")
h.write(ans)
h.close()


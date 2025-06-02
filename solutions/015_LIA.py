from math import factorial as f

# Probability of >= N individuals in kth generation being AaBb is
# Sum from i=N to 2^k of 2^k choose i times
def getProbOffspring(k: int, N: int) -> float:
    prob = 0.0
    P = 2**k
    for i in range(N, P+1):
        prob += ( f(P) / (f(i) * f(P-i)) ) * (0.25)**i * (0.75)**(P-i)
    return prob


# Return a tuple (k, n)
def parseInput(file):
    k, n = map(int, file.read().split())
    return (k, n)

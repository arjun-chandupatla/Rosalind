

def f(x: int) -> int:
    prod = 1
    for i in list(range(1, x+1)):
        prod *= i
    return prod


def getProbOffspring(k: int, N: int) -> float:
    prob = 0.0
    P = 2**k
    for i in range(N, P+1):
        prob += ( f(P) / (f(i) * f(P-i)) ) * (0.25)**i * (0.75)**(P-i)
    return prob



def parseInput(file):
    k, n = map(int, file.read().split())
    return (k, n)

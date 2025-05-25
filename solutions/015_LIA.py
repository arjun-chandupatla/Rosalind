

def f(x: int) -> int:
    prod = 1
    for i in list(range(1, x+1)):
        prod *= i
    return prod

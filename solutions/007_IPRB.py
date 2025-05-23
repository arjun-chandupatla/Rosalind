# Mendel's First Law
# probabilities mostly


def dominant(k: int, m: int, n: int) -> float:
    Pr1 = lambda x: x/float(k+m+n)
    Pr2 = lambda x: x/float(k+m+n-1)
    sum = 0
    sum += Pr1(k)
    sum += (Pr1(m) * Pr2(k)) + (0.75)*(Pr1(m) * Pr2(m-1)) + (0.5)*(Pr1(m) * Pr2(n))
    sum += (Pr1(n)*Pr2(m)) + 0.5*(Pr1(n) * Pr2(m))
    return sum

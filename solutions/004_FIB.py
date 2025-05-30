def fib(n: int, k: int) -> int:
    numPairs = [1, 1]
    for i in range(2, n):
        numPairs.append(k*numPairs[i-2] + numPairs[i-1])
    return numPairs[-1]

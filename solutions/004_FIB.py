def fib(n: int, k: int) -> int:
    numPairs = [1, 1]
    i = 2
    while i < n:
        numPairs.append(k*numPairs[i-2] + numPairs[i-1])
        i+=1
    return numPairs[-1]

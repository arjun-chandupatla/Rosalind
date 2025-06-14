# Similar problem to 004_FIB, but rabbits die after m months
# More accurate modeling of the rabbit population
# Relies on dynamic programming ideas

def fibd(n, m):
    f = [1, 1]
    i = 2
    for i in range(m):
        f.append(f[i-2] + f[i-1])

    for j in range(m + 1, n+1):
        f.append(sum(f[j-m-1:j-2]))
    return(f[-1])

from itertools import product

# List all possible permutations of the alphabet provided
def enumeratePerms(alph: list[str], n: int) -> list[str]:
    perms = []
    for i in range(1, n + 1):
        perms += list("".join(tup) for tup in product(alph, repeat=i))
    return perms


# Sort the permutations list lexicographically
def sortPerms(perms, alph, n):
    map = dict()
    map["0"] = ""

    # Converts each string to a sequence of (hexadecimal) numbers
    # to allow for the list to be sorted
    for i in range(len(alph)):
        map[alph[i]] = hex(i+1)[2:]
        map[hex(i+1)[2:]] = alph[i]
    
    nperms = list()
    for p in perms:
        temp = ""
        for char in p:
            temp += map[char]
        if (len(temp) < n):
            temp += (n - len(temp)) * "0"
        nperms.append(temp)
    nperms.sort()    # Uses Python's list.sort() to sort the numerical list

    sorted = list()

    for np in nperms:
        temp = ""
        for num in np:
            temp += map[num]
        sorted.append(temp)

    return sorted


# One single function to both enumerate and return the sorted list of permutations
def getPerms(alph: list[str], n: int) -> list[str]:
    perms = enumeratePerms(alph, n)
    perms = sortPerms(perms, alph, n)
    return perms
        

# Parse the input txt file from Rosalind
def parseInput(file):
    text = file.read()
    return (text.split()[:-1], int(text.split()[-1]))


# Format the output for the Rosalind autograder
def formatOutput(perms: list[str]) -> str:
    return "\n".join(perms)



if __name__ == "__main__":
    i = open("input.txt", "r")
    alph, n = parseInput(i)
    i.close()

    ans = getPerms(alph, n)

    o = open("output.txt", "w")
    o.write(ans)
    o.close()

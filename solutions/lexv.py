
import itertools

def enumeratePerms(alph: list[str], n: int) -> list[str]:
    perms = []
    for i in range(1, n + 1):
        perms += list("".join(tup) for tup in itertools.product(alph, repeat=i))
    return perms


def asdfasdf(perms, alph, n):
    map = dict()
    map["0"] = ""

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
    nperms.sort()

    sorted = list()

    for np in nperms:
        temp = ""
        for num in np:
            temp += map[num]
        sorted.append(temp)

    return sorted


def getPerms(alph: list[str], n: int) -> list[str]:
    perms = enumeratePerms(alph, n)
    perms = asdfasdf(perms, alph, n)
    return perms
    

    

def parseInput(file):
    text = file.read()
    return (text.split()[:-1], int(text.split()[-1]))


def formatOutput(perms: list[str]) -> str:
    return "\n".join(perms)



if __name__ == "__main__":
    i = open("input.txt", "r")
    alph, n = parseInput(i)
    i.close()

    perms = enumeratePerms(alph, n)
    s = asdfasdf(perms, alph, n)

    ans = formatOutput(s)

    o = open("output.txt", "w")
    o.write(ans)
    o.close()

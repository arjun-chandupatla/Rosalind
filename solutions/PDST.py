def dist(s1: str, s2: str) -> float:
    if s1 == s2:
        return 0.0
    num = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            num += 1
    return num/len(s1)


def distMatrix(arr: list[str]) -> list[list[float]]:
    matrix = [[0.0 for _ in range(len(arr))] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            matrix[i][j] = dist(arr[i], arr[j])
    return matrix


def formatOutput(matrix: list[list[float]]):
    s = ""
    for r in matrix:
        s += " ".join([str(item) for item in r]) + "\n"
    return s


def parseInput(file):
    temp = ""
    arr = []
    for line_s in file.readlines()[1:]:
        line = line_s.strip()
        if line.startswith(">"):
            arr.append(temp)
            temp = ""
        else:
            temp += line
    arr.append(temp)
    return arr

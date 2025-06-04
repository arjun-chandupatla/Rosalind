# Given a positive integer n ≤ 1000 and an adjacency list for a graph with n nodes and no cycles,
# return the minimum number of edges that can be added to this graph to make a tree


def parseInput(file):
    lines = file.readlines()
    n = int(lines[0].strip())
    l = list()
    temp = []
    for i in range(1, len(lines)):
        line = lines[i].strip()
        l.append([int(j) for j in line.split()])
    
    return (n, l)

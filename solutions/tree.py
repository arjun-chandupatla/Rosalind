# Given a positive integer n ≤ 1000 and an adjacency list for a graph with n nodes and no cycles,
# return the minimum number of edges that can be added to this graph to make a tree




def func(n, edge_list: list[list[int]]) -> int:
    num = 0
    temp = []
    for edge in edge_list:
        temp += edge
    for i in range(1, n + 1):
        if i not in set(temp):
            num += 1
    

    l = [edge_list[0]]
    for i in range(1, len(edge_list)):
        [e1, e2] = edge_list[i]
        test = 1
        idx = []

        for j in range(len(l)):
            item = l[j]

            if e1 in item and e2 not in item:
                item.append(e2)
                idx.append(j)
                test = 0

            elif e2 in item and e1 not in item:
                item.append(e1)
                idx.append(j)
                test = 0

        if test == 1:
            l.append([e1, e2])
        if len(idx) > 1:
            id0 = idx[0]
            for k in range(len(idx) - 1, 0, -1):
                idk = idx[k]
                l[id0] += l[idk]
                del l[idk]


    num += len(l) - 1


    return num








def parseInput(file):
    lines = file.readlines()
    n = int(lines[0].strip())
    l = list()
    temp = []
    for i in range(1, len(lines)):
        line = lines[i].strip()
        l.append([int(j) for j in line.split()])
    
    return (n, l)



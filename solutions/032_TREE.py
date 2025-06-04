# Given a positive integer n ≤ 1000 and an adjacency list for a graph with n nodes and no cycles,
# return the minimum number of edges that can be added to this graph to make a tree


def countNumEdges(n, edge_list: list[list[int]]) -> int:
    num = 0     # Number of edges that need to be added

    # If a number is less than n but not in the adjacency list, then it is isolated
    # and needs an edge to connect it to the rest of the tree
    temp = []
    for edge in edge_list:
        temp += edge

    for i in range(1, n + 1):
        if i not in set(temp):
            num += 1

    # Essentially transitive closure
    l = [edge_list[0]]

    for i in range(1, len(edge_list)):
        [e1, e2] = edge_list[i]
        test = 1        # This is used to test if an item is connected, or needs an edge to connect it
        idx = []

        for j in range(len(l)):
            item = l[j]

            # Check if connections exist
            if e1 in item and e2 not in item:
                item.append(e2)
                idx.append(j)   # idx used to check for further connections
                test = 0

            elif e2 in item and e1 not in item:
                item.append(e1)
                idx.append(j)
                test = 0

        if test == 1:       # If there are no connections, append it to l
            l.append([e1, e2])

        if len(idx) > 1:    # If two sublists share an element, then merge them
            id_0 = idx[0]
            for k in range(len(idx) - 1, 0, -1):
                id_k = idx[k]
                l[id_0] += l[id_k]
                del l[id_k]

    num += len(l) - 1       # Number of connections, not the number of separate graphs
    
    return num


# Take input file and convert to an integer and a list of edges
def parseInput(file):
    lines = file.readlines()
    n = int(lines[0].strip())
    l = list()
    for i in range(1, len(lines)):
        line = lines[i].strip()
        l.append([int(j) for j in line.split()])
    
    return (n, l)

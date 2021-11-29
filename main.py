import sys

EDGE_ID = 0
START_NODE = 1
END_NODE = 2
LENGTH = 3


def stringToInt(edge):
    for i in range(len(edge) - 1):
        edge[i] = int(edge[i])
    edge[3] = float(edge[3])
    return edge

def main():
    edges = []

    with open('small_test.txt') as f:
        for line in f:
            edges.append(line.split(" "))

    vert_count = 0
    for edge in edges:
        stringToInt(edge)
        if edge[START_NODE] >= vert_count or edge[END_NODE] >= vert_count:
            if edge[START_NODE] > edge[END_NODE]:
                vert_count = edge[START_NODE]
            else:
                vert_count = edge[END_NODE]


    print(vert_count)

    graph = {}

    for edge in edges:
        if edge[START_NODE] not in graph:
            graph[edge[START_NODE]] = []
        if edge[END_NODE] not in graph:
            graph[edge[END_NODE]] = []

        graph[edge[START_NODE]].append([edge[EDGE_ID],edge[END_NODE],edge[LENGTH]])

    print(graph)

    #return graph

main()


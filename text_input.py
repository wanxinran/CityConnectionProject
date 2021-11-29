import sys

EDGE_ID = 0
START_NODE = 1
END_NODE = 2
LENGTH = 3


def main():
    edges = []

    with open(sys.argv[1]) as f:
        for line in f:
            edges.append(line.split(" "))

    vert_count = 0
    for edge in edges:
        if edge[START_NODE] >= vert_count or edge[END_NODE] >= vert_count:
            if edge[START_NODE] > edge[END_NODE]:
                vert_count = edge[START_NODE]
            else:
                vert_count = edge[END_NODE]

    graph = [0] * vert_count

    for edge in edges:
        graph[edge[START_NODE]] = [edge[EDGE_ID]][edge[END_NODE]][edge[LENGTH]]

    print(graph)

    return graph




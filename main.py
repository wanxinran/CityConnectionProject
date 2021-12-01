import sys

EDGE_ID = 0
START_NODE = 1
END_NODE = 2
LENGTH = 3

class Graph:

    def stringToInt(self, edge):
        for i in range(len(edge) - 1):
            edge[i] = int(edge[i])
        edge[3] = float(edge[3])
        return edge

    def printGraph(self, graph):
        print("Number of vertices: " + str(self.vert_count) + "\n")
        print("________________________Format________________________")
        print("| START NODE  |" + " ------> " + "| [EDGE ID, END NODE, LENGTH] |")
        for key in range(len(graph)):
            print("| " + str(graph.keys()[key]) + " |" + " ------> " + "| " + str(graph.values()[key]) +  " |")

    def createGraph(self):
        edges = []

        with open('small_test.txt') as f:
            for line in f:
                edges.append(line.split(" "))

        self.vert_count = 0
        for self.edge in edges:
            self.stringToInt(self.edge)
            if self.edge[START_NODE] >= self.vert_count or self.edge[END_NODE] >= self.vert_count:
                if self.edge[START_NODE] > self.edge[END_NODE]:
                    self.vert_count = self.edge[START_NODE]
                else:
                    self.vert_count = self.edge[END_NODE]


        graph = {}

        for self.edge in edges:
            if self.edge[START_NODE] not in graph:
                graph[self.edge[START_NODE]] = []
            if self.edge[END_NODE] not in graph:
                graph[self.edge[END_NODE]] = []

            graph[self.edge[START_NODE]].append([self.edge[EDGE_ID],self.edge[END_NODE],self.edge[LENGTH]])

        return graph


if __name__ == '__main__':
    graph = Graph()
    graph_data = graph.createGraph()
    graph.printGraph(graph_data)
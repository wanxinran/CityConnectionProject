import sys

class Edge:
    id: int
    startNode: int
    endNode: int
    weight: float

    def __init__(self, id, start,end,weight) -> None:
        self.id = id
        self.startNode = start
        self.endNode=end
        self.weight = weight

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return '{} {} {} {}'.format(self.id, self.startNode, self.endNode, self.weight)

class CityConnections:
    def load(file):
        E = []
        V = []
        with open(file, "r") as f:
            for line in f:
                if '#' not in str(line):
                    id,start,end,weight = line.split(" ")
                    edge = Edge(int(id), int(start), int(end), float(weight))
                    if edge.startNode not in V:
                        V.append(edge.startNode)
                    if edge.endNode not in V:
                        V.append(edge.endNode)
                    E.append(edge)
        return V,E
    
    def write(edges, file, comments:list=[]):
        with open(file, "w") as f:
            if len(comments) > 0:
                for comment in comments:
                    f.write('#{}'.format(comment))
                    f.write('\n')

            lines = [str(x) for x in edges]
            f.write(lines[0])
            for line in lines[1:]:
                f.write('\n')
                f.write(line)

    def toAdjacencyList(E):
        adjList = {}
        for edge in E:
            if edge.startNode not in adjList:
                adjList[edge.startNode] = []
            if edge.endNode not in adjList:
                adjList[edge.endNode] = []
            adjList[edge.endNode].append((edge.startNode, edge.weight, edge.id))
            adjList[edge.startNode].append((edge.endNode, edge.weight, edge.id))
        return adjList
    
    def toAdjacencyMatrix(V:list,E:list):
        G_id = [[0 for _ in range(len(V))] for _ in range(len(V))]
        G = [[0 for _ in range(len(V))] for _ in range(len(V))]
        for edge in E:
            x = V.index(edge.startNode)
            y = V.index(edge.endNode)
            G[x][y] = edge.weight
            G[y][x] = edge.weight
            G_id[x][y] = edge.id
            G_id[y][x] = edge.id
        return G, G_id
    
    def implementation1(V, E, debug=False):
        G, G_ID = CityConnections.toAdjacencyMatrix(V,E)
        MST = CityConnections.primsMST(G, G_ID, V, debug=debug)
        return MST
            
    def primsMST(G, G_ID, V, INF = 99999999999, debug=False):
        '''Accepts an NxN adjacency matrix G.
        Additionally an NxN matrix of edge ids with size NxN, an a list V of node ids should be supplied.

        Time complexity: O(E log V)'''
        #n number of verticies
        n = len(V)
        #Tracks selected vertex
        selected = [False for _ in range(n)]
        #Number of MST edges
        numEdges = 0
        #Select first vertex
        selected[0] = True

        #MST output collection
        output = [None] * (n-1)
        while (numEdges < n-1):
            
            if (debug and numEdges % 100 == 0): print('{}%'.format(numEdges/(n-1)*100))
            # 1) For every vertex, find all adjacent vertices
            # 2) Calculate distance from vertex
            #    a) If vertex already previously selected discard result
            # 3) Choose another vertex and repeat
            minimum = INF
            x,y = 0,0
            for i in range(n):
                if selected[i]:
                    for j in range(n):
                        if ((not selected[j]) and G[i][j]):
                            #Not already selected, and edge exists
                            if minimum > G[i][j]:
                                minimum = G[i][j]
                                x,y = i,j     
            output[numEdges] = Edge(G_ID[x][y], V[x],V[y],G[x][y])
            # output.append(Edge(G_ID[x][y], V[x],V[y],G[x][y]))
            selected[y] = True
            numEdges += 1
        return output

    def totalWeight(E: list):
        return sum(e.weight for e in E)


if __name__ == '__main__':
    if (len(sys.argv[1:]) == 2):
        inputFile, outputFile = sys.argv[1], sys.argv[2]
        V,E = CityConnections.load('./input.txt')
        MST = CityConnections.implementation1(V,E)
        total = sum(e.weight for e in MST)
        CityConnections.write(MST, outputFile, ['Total: {}'.format(total)])
    else:
        print('Need input file and output file arguments', sys.argv[1:])





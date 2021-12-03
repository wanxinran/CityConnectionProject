import sys

'''
Class for Edge object.
'''
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

'''
Class includes graph representation and algorithms for MSP.
'''
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
    
    def implementation1(V, E):
        '''
        Graph representation: adjacency matrix
        Algorithm for MSP: Prim's
        Data structure used for the algorithm: matrix
        '''
        G, G_ID = CityConnections.toAdjacencyMatrix(V,E)
        MST = CityConnections.primsMST(G, G_ID, V)
        return MST
    
    def implementation2(V, E):
        '''
        Graph representation: two lists - V and E
        Algorithm for MSP: Kruskal's
        Data structure used for the algorithm: disjoint set
        '''
        MST = CityConnections.kruskalMST(V, E)
        return MST
            
    def primsMST(G, G_ID, V, INF = 99999999999):
        '''
        Accepts an NxN adjacency matrix G.
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
        output = []

        while (numEdges < n-1):
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
            output.append(Edge(G_ID[x][y], V[x],V[y],G[x][y]))
            selected[y] = True
            numEdges += 1
        return output
    
    def kruskalMST(V, E):
        '''
        Input: list of vertices, and list of Edges
        Output: a list of MST using Kruskal's algorithm.
        Runtime: O(E log V) using disjoint set.
        '''
        
        # define some functions to use
        def findParent(parent, i):
            '''
            Find the parent node for node i.
            '''
            if parent[i] == i:
                return i
            else:
                return findParent(parent, parent[i])
            
        def unionSets(parent, rank, x, y):
            '''
            Union two sets of x and y
            '''
            xr = findParent(parent, x)
            yr = findParent(parent, y)
            if rank[xr] < rank[yr]:
                parent[xr] = yr
            elif rank[yr] > rank[xr]:
                parent[yr] = xr
            else:
                parent[yr] = xr
                rank[xr] += 1
        
        MSP = []
        i, edgeCounter = 0, 0
        
        # 1) sort all edges in non-decreasing order
        E = sorted(E, key=lambda edge: edge.weight)
        
        parent = []
        rank = []
        
        # Create sets to be used later for disjoint sets
        for n in range(len(V)):
            parent.append(n)
            rank.append(0)
        
        # 2) Go through every edge in sorted order
        #   a) If adding an edge doesn't create a cycle: add edge to MST
        while edgeCounter < len(V) - 1:
            u, v = E[i].startNode, E[i].endNode
            x = findParent(parent, u)
            y = findParent(parent, v)
            
            if x != y:
                edgeCounter += 1
                MSP.append(E[i])
                unionSets(parent, rank, x, y)
            i += 1
                
        return MSP
            
            
        

if __name__ == '__main__':
    if (len(sys.argv[1:]) == 2):
        inputFile, outputFile = sys.argv[1], sys.argv[2]
        V,E = CityConnections.load(inputFile)
        # 1st implementation
        MST1 = CityConnections.implementation1(V,E)
        total = sum(e.weight for e in MST1)
        CityConnections.write(MST1, outputFile, ['Total: {}'.format(total)])
        
        # 2nd implementation
        MST2 = CityConnections.implementation2(V, E)
        total = sum(e.weight for e in MST2)
        CityConnections.write(MST2, outputFile, ['Total: {}'.format(total)])
        
    else:
        print('Need input file and output file arguments', sys.argv[1:])





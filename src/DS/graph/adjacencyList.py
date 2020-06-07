"""
Python3 program implements graph representation in adjacencyList 
"""
from collections import defaultdict

#graph class
class Graph:
    #constructore
    def __init__(self):
        self.graph = defaultdict(list)

    # function add edge into graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # print graph node connected with each vertices.
    def printGraph(self):
        for i in self.graph:
            print(self.graph[i])

# Driver code
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3)
    g.printGraph()
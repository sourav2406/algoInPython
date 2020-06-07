from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, s, visited):
        visited[s] = True
        print(s, end=' ')

        for i in self.graph[s]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self):
        visited = [False] * (len(self.graph))

        for i in self.graph:
            if visited[i] == False:
                self.DFSUtil(i, visited)

if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3) 
    
    print("Following is DFS from (starting from vertex 2)") 
    g.DFS()
    print("\n")
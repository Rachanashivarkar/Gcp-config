class Edge:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for edge in edges:
            self.adjList[edge.source].append(edge.dest)
            self.adjList[edge.dest].append(edge.source)

def DFS(graph, v, discovered):
    discovered[v] = True
    print(v, end=' ')
    for u in graph.adjList[v]:
        if not discovered[u]:
            DFS(graph, u, discovered)

if __name__ == '__main__':
    edges = [
        Edge(1, 2), Edge(1, 7), Edge(1, 8), Edge(2, 3),
        Edge(2, 6), Edge(3, 4), Edge(3, 5), Edge(8, 9),
        Edge(8, 12), Edge(9, 10), Edge(9, 11)
    ]
    n = 13
    graph = Graph(edges, n)
    discovered = [False] * n
    for i in range(n):
        if not discovered[i]:
            DFS(graph, i, discovered)

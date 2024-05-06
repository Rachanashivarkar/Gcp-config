from collections import deque

class EdgeBFS:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

class Graph:
    def __init__(self, edges, n):
        self.adjList = [[] for _ in range(n)]
        for edge in edges:
            self.adjList[edge.source].append(edge.dest)
            self.adjList[edge.dest].append(edge.source)

def recursiveBFS(graph, q, discovered):
    if not q:
        return
    v = q.popleft()
    print(v, end=' ')
    for u in graph.adjList[v]:
        if not discovered[u]:
            discovered[u] = True
            q.append(u)
    recursiveBFS(graph, q, discovered)

if __name__ == '__main__':
    edges = [EdgeBFS(1, 2), EdgeBFS(1, 3), EdgeBFS(1, 4), EdgeBFS(2, 5),
             EdgeBFS(2, 6), EdgeBFS(5, 9), EdgeBFS(5, 10), EdgeBFS(4, 7),
             EdgeBFS(4, 8), EdgeBFS(7, 11), EdgeBFS(7, 12)]
    n = 15
    graph = Graph(edges, n)
    discovered = [False] * n
    q = deque()
    for i in range(n):
        if not discovered[i]:
            discovered[i] = True
            q.append(i)
            recursiveBFS(graph, q, discovered)

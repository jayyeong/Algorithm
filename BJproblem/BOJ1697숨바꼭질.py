from collections import deque

def bfs():
    graph = deque()
    graph.append([N,0])
    visited = list()

    while graph:

        node = graph[0][0]
        depth = graph[0][1]
        graph.popleft()

        if node == K:
            return depth

        if node - 1 >= 0 and node - 1 <= 100000 and node - 1 not in visited:
            visited.append(node - 1)
            graph.append([node - 1,depth + 1])
        if node + 1 >= 0 and node + 1 <= 100000 and node + 1 not in visited:
            visited.append(node + 1)
            graph.append([node + 1,depth + 1])
        if node * 2 >= 0 and node * 2 <= 100000 and node * 2 not in visited:
            visited.append(node * 2)
            graph.append([node * 2,depth + 1])


N, K = map(int,input().split())
print(bfs())


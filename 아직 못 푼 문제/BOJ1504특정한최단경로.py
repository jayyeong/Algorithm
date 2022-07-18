

INF = int(1e9)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
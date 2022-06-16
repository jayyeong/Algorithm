import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
graph = [[] for y in range(V + 1)]

INF = int(1e9)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

#print(graph)
D = [INF] * (V + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    D[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if D[now] < dist:
            continue
        for i in graph[now]: # 0: dist 1: weight
            cost = dist + i[1]
            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(K)

for i in range(1, V + 1):
    if D[i] == INF:
        print('INF')
    else:
        print(D[i])


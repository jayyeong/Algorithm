import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for i in range(N + 1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

st, ed = map(int,input().split())
INF = int(1e9)
D = [INF] * (N + 1)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    D[start]
    while q:
        dist, now = heapq.heappop(q)
        if D[now] < dist:
            continue
        for i in graph[now]: # 0: dist 1: weight
            cost = dist + i[1]
            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(st)

print(D[ed])
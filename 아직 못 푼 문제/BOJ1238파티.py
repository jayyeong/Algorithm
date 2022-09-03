import heapq
import sys
INF = int(1e9)

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, T = map(int, sys.stdin.readline().split())
    graph[A].append([B, T])

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    D[start] = 0

    while que:
        dist, now = heapq.heappop(que)
        if D[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

ans = [0] * (N + 1)

for i in range(1, N + 1):
    D = [INF] * (N + 1)
    dijkstra(i)
    if i == X:
        for j in range(1, N + 1):
            ans[j] += D[j]
    else:
        ans[i] += D[X]

print(max(ans))
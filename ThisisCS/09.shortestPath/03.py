import sys, heapq
INF = int(1e9)

N, M, C = map(int,input().split())

graph = [[] for _ in range(N + 1)]

distance = [INF] * (N + 1)

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)
total_city, total_time = 0, 0

for i in range(1, N + 1):
    if distance[i] != INF and i != C:
        total_city += 1
        total_time = max(distance[i], total_time)

print(total_city, total_time)

import sys, heapq

V, E = map(int,input().split())

K = int(input())

graph = [[] for y in range(V + 1)]

INF = int(1e9)
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((v,w)) #u에서 v까지 갈때 걸리는 비용 w

#print(graph)

D = [INF] * (V + 1)

def dijkstra(start):
    qq = []
    heapq.heappush(qq,(0,start)) #(거리, 시작점) 자기자신은 거리가 0

    while qq:
        dist, now = heapq.heappop(qq)
        if D[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < D[i[0]]:
                D[i[0]] = cost
                heapq.heappush(qq, (cost,i[0]))

dijkstra(K)
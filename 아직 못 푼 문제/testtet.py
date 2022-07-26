import sys, heapq
INF = int(1e9)


N, E = map(int,input().split())

cost = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    cost[i][i] = 0

for i in range(E):
    a, b, c = map(int,sys.stdin.readline().rstrip().split())
    if cost[a][b] > c:
        cost[a][b] = c
        cost[b][a] = c

v1, v2 = map(int,input().split())

for k in range(N + 1):
    for i in range(N + 1):
        for j in range(N + 1):
            cost[i][j] = min(cost[i][j],cost[i][k] + cost[k][j])


print(min(cost[1][v1] + cost[v1][v2] + cost[v2][N], cost[1][v2] + cost[v2][v1] + cost[v1][N]))
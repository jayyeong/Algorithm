import sys
N, E = map(int,input().split())
INF = int(1e9)

graph = [[INF] * (N + 1) for i in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().split())

for i in graph:
    print(i)

start = 1
end = N

def dfs(n):

for i in graph:
    print(i)


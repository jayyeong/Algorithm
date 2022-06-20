import sys
sys.setrecursionlimit(10**5)
N, M = map(int,input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int,sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(N + 1)]
# print(graph)
def dfs(n):
    visited[n] = True

    for node in graph[n]:
        if visited[node] == False:
            dfs(node)

count = 0
for i in range(1,N + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
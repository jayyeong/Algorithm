import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
leafnode = [x for x in range(1,N + 1)]

for _ in range(N - 1):
     x,y,z = map(int,input().split())
     graph[x].append([y,z])
     graph[y].append([x,z])

# print(graph)
# print(leafnode)

distance = [-1] * (N + 1)
distance[1] = 0
box = []
def dfs(n,c):
    for i in graph[n]:
        if distance[i[0]] == -1:
            distance[i[0]] = c + i[1]
            dfs(i[0],c + i[1])
dfs(1,0)
#print(distance)

start = distance.index(max(distance))

distance = [-1] * (N + 1)
distance[start] = 0
dfs(start,0)

print(max(distance))
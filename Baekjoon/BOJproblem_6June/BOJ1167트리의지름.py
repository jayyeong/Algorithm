from collections import deque
V = int(input())

graph = [[] for _ in range(V + 1)]
distance = [-1] * (V + 1)
distance[1] = 0
for _ in range(V):
    deq = deque([int(x) for x in input().rstrip('-1').split()])
    node = deq.popleft()
    while deq:
        x = deq.popleft()
        y = deq.popleft()
        graph[node].append([x,y])

def dfs(n,c):
    for i in graph[n]:
        if distance[i[0]] == -1:
            distance[i[0]] = c + i[1]
            dfs(i[0],c + i[1])
dfs(1,0)
s = distance.index(max(distance))
distance = [-1] * (V + 1)
distance[s] = 0
dfs(s,0)
print(max(distance))
#print(graph)
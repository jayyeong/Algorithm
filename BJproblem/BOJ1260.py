from collections import deque

N, M, V = map(int,input().split())
boxs = []
for _ in range(M):
    boxs.append(list(map(int,input().split())))
#print(boxs)
#입력
graph = []
for x in range(N + 1):
    graph.append([])
for box in boxs:
    graph[box[0]].append(box[1])
    graph[box[1]].append(box[0])

for g in graph:
    g.sort()

#print(graph)
# 그래프 만들기
visited = [False] * (N + 1)
visitedB = [False] * (N + 1)

def dfs(topN,graph,visited):
    visited[topN] = True
    print(topN,end = ' ')
    for x in graph[topN]:
        if not visited[x]:
            dfs(x, graph, visited)


def bfs(topNB,graphB,visitedB):
    queue = deque([topNB])
    visitedB[topNB] = True

    while queue:
        v = queue.popleft()
        print(v,end = ' ')

        for x in graphB[v]:
            if not visitedB[x]:
                queue.append(x)
                visitedB[x] = True

dfs(V,graph,visited)
print()
bfs(V,graph,visitedB)
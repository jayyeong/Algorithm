def dfs(start,visited = []):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(node,visited)

    return visited

ComNum = int(input())
PairNum = int(input())
arr = []
visited = []
for _ in range(PairNum):
    arr.append([int(x) for x in input().split()])
#print(tree)
graph = [[] for i in range(ComNum + 1)]
#print(graph)
for i in range(ComNum + 1):
    for a in arr:
        if i in a:
            if i == a[0]:
                graph[i].append(a[1])
            else:
                graph[i].append(a[0])
#print(graph)

print(len(dfs(1)) - 1)

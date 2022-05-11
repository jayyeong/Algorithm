
def getSmallIndex():
    min = 11
    index = 0
    for i in range(V):
        if D[i] < min and not v[i]:
            min = D[i]
            index = i
    return index

def Dijkstra(start):
    for i in range(V):
        D.append(graph[start][i])
    v[start] = True
    for i in range(V - 2):
        current = getSmallIndex()
        v[current] = True
        for j in range(V):
            if not v[j]:
                if D[current] + graph[current][j] < D[j]:
                    D[j] = D[current] + graph[current][j]

V, E = map(int, input().split())
K = int(input())
graph = [[11 if x != y else 0 for x in range(V)] for y in range(V)]

for _ in range(E):
    u, v, w = map(int, input().split())
    if graph[u - 1][v - 1] > w:
        graph[u - 1][v - 1] = w

#print(graph)
v = [False for _ in range(V)]
D = []

Dijkstra(K - 1)
for d in D:
    if d == 11:
        print('INF')
    else:
        print(d)

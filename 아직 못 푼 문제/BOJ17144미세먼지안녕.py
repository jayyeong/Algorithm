import sys
R, C, T = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

air_filter = []

graph = []
for i in range(R):
    graph.append([int(x) for x in sys.stdin.readline().split()])
    if graph[i][0] == -1:
        air_filter.append([i,0])

print(air_filter)

def Spread():
    temp = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            count = 0
            if graph[i][j] > 0:
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        temp[nx][ny] += graph[i][j] // 5
                        count += 1
                temp[i][j] += graph[i][j] - (graph[i][j] // 5) * count

    return temp

def running():
    pass

def aggregate():
    for i in range(R):
        for j in range(C):
            graph[i][j]

for _ in range(T):
    graph = Spread()
    running()

aggregate()
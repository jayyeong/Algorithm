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

#print(air_filter)

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
    ax, ay = air_filter[0]

    for i in range(ax - 1, -1, -1):
        graph[i + 1][0] = graph[i][0]

    for i in range(0, C - 1):
        graph[0][i] = graph[0][i + 1]

    for i in range(0, ax):
        graph[i][C - 1] = graph[i + 1][C - 1]

    for i in range(C - 2, 0, -1):
        graph[ax][i + 1] = graph[ax][i]

    graph[ax][0] = 0
    graph[ax][1] = 0

    ax2, ay2 = air_filter[1]

    for i in range(ax2, R - 1):
        graph[i][0] = graph[i + 1][0]

    for i in range(0, C - 1):
        graph[R - 1][i] = graph[R - 1][i + 1]

    for i in range(R - 2, ax2 - 1, - 1):
        graph[i + 1][C - 1] = graph[i][C - 1]

    for i in range(C - 2, 0, - 1):
        graph[ax2][i + 1] = graph[ax2][i]

    graph[ax2][1] = 0
    graph[ax2][0] = 0

def aggregate():
    ans = 0
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                ans += graph[i][j]
    return ans

for _ in range(T):
    graph = Spread()
    running()

print(aggregate())
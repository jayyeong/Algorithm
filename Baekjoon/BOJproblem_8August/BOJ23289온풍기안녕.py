import sys
from collections import deque

R, C, K = map(int, input().split())

graph = []
checking_area = []
heater = []

# 오 왼 위 아래
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(R):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(C):
        if 0 < graph[i][j] < 5:
            heater.append([graph[i][j] - 1, i, j])
            graph[i][j] = 0

        elif graph[i][j] == 5:
            checking_area.append([i, j])
            graph[i][j] = 0


W = int(input())

wall_list = []

for _ in range(W):
    wall_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

wallHori = [[0] * C for _ in range(R)]

wallVer = [[0] * C for _ in range(R)]

for w in wall_list:
    if w[2] == 0:
        wallHori[w[0] - 1][w[1] - 1] = -1
    else:
        wallVer[w[0] - 1][w[1] - 1] = 1

def wind():
    for h in heater:
        hd, hx, hy = h

        tem = diffuse(hd, hx, hy)

        for i in range(R):
            for j in range(C):
                graph[i][j] += tem[i][j]

def diffuse(md, mx, my):
    # x, y = mr, mc
    temp = [[0] * C for _ in range(R)]
    q = deque([])
    x, y = mx + dx[md], my + dy[md]
    temp[x][y] = 5
    q.append([x, y, 5])
    while q:
        x, y, t = q.popleft()
        if t < 1:
            return temp
        if md == 0:  # 오른쪽
            if upCh(x, y, 2):
                if rightCh(x - 1, y, md):
                    q.append([x - 1, y + 1, t - 1])
                    temp[x - 1][y + 1] = t - 1
            if rightCh(x, y, md):
                q.append([x, y + 1, t - 1])
                temp[x][y + 1] = t - 1
            if downCh(x, y, 3):
                if rightCh(x + 1, y, md):
                    q.append([x + 1, y + 1, t - 1])
                    temp[x + 1][y + 1] = t - 1

        elif md == 1:  # 왼쪽
            if upCh(x, y, 2):
                if leftCh(x - 1, y, md):
                    q.append([x - 1, y - 1, t - 1])
                    temp[x - 1][y - 1] = t - 1
            if leftCh(x, y, md):
                q.append([x, y - 1, t - 1])
                temp[x][y - 1] = t - 1
            if downCh(x, y, 3):
                if leftCh(x + 1, y, md):
                    q.append([x + 1, y - 1, t - 1])
                    temp[x + 1][y - 1] = t - 1

        elif md == 2:
            if leftCh(x, y, 1):
                if upCh(x, y - 1, md):
                    q.append([x - 1, y - 1, t - 1])
                    temp[x - 1][y - 1] = t - 1
            if upCh(x, y, md):
                q.append([x - 1, y, t - 1])
                temp[x - 1][y] = t - 1
            if rightCh(x, y, 0):
                if upCh(x, y + 1, md):
                    q.append([x - 1, y + 1, t - 1])
                    temp[x - 1][y + 1] = t - 1

        elif md == 3:
            # q = downCheck(x, y, t, md, temp, q)
            if leftCh(x, y, 1):
                if downCh(x, y - 1, md):
                    q.append([x + 1, y - 1, t - 1])
                    temp[x + 1][y - 1] = t - 1
            if downCh(x, y, md):
                q.append([x + 1, y, t - 1])
                temp[x + 1][y] = t - 1
            if rightCh(x, y, 0):
                if downCh(x, y + 1, md):
                    q.append([x + 1, y + 1, t - 1])
                    temp[x + 1][y + 1] = t - 1
    return temp

def rightCh(x, y, i):
    if wallVer[x][y] == 1:
        return False
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < R and 0 <= ny < C:
        #if not visited[nx][ny]:
        return True
    return False

def leftCh(x, y, i):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < R and 0 <= ny < C:
        #if not visited[nx][ny] and wall[nx][ny] == 1:
        if wallVer[nx][ny] != 1:
            return True
    return False

def upCh(x, y, i):
    if wallHori[x][y] == -1:
        return False
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < R and 0 <= ny < C:
        #if not visited[nx][ny]:
        return True
    return False

def downCh(x, y, i):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < R and 0 <= ny < C:
        #if not visited[nx][ny] and wall[nx][ny] == -1:
        if wallHori[nx][ny] != -1:
            return True
    return False

def adjust():
    temp = [[0] * C for _ in range(R)]
    visited = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if rightCh(x, y, 0):
                dif = graph[x][y] - graph[x][y + 1]
                if dif > 0:
                    ad = dif//4
                    if ad > 0:
                        temp[x][y] -= ad
                        temp[x][y + 1] += ad

            if leftCh(x, y, 1):
                dif = graph[x][y] - graph[x][y - 1]
                if dif > 0:
                    ad = dif // 4
                    if ad > 0:
                        temp[x][y] -= ad
                        temp[x][y - 1] += ad

            if upCh(x, y, 2):
                dif = graph[x][y] - graph[x-1][y]
                if dif > 0:
                    ad = dif // 4
                    if ad > 0:
                        temp[x][y] -= ad
                        temp[x - 1][y] += ad

            if downCh(x, y, 3):
                dif = graph[x][y] - graph[x+1][y]
                if dif > 0:
                    ad = dif // 4
                    if ad > 0:
                        temp[x][y] -= ad
                        temp[x + 1][y] += ad
            #visited[x][y] = 1
    for x in range(R):
        for y in range(C):
            graph[x][y] += temp[x][y]

def reduction():
    for j in range(C):
        if graph[0][j] > 0:
            graph[0][j] -= 1
    for j in range(C):
        if graph[-1][j] > 0:
            graph[R - 1][j] -= 1

    for i in range(1, R - 1):
        if graph[i][0] > 0:
            graph[i][0] -= 1
        if graph[i][-1] > 0:
            graph[i][-1] -= 1

def condition_check():
    for a in checking_area:
        x, y = a
        if graph[x][y] < K:
            return True
    return False

ans = 0

while True:

    wind()
    adjust()
    reduction()

    ans += 1

    if condition_check() == False:
        break

print(ans)
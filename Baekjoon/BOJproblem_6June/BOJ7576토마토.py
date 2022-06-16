from collections import deque

M, N = map(int,input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

box = [] # 1 익은 토, 0 안익은 토, -1 빈 칸
day = [[0 for _ in range(M)] for _ in range(N)]

deq = deque()

for i in range(N):
    box.append([int(x) for x in input().split()])
    for j in range(M):
        if box[i][j] == 1:
            deq.append([i,j])

while deq:
    x, y = deq.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if box[nx][ny] == 0:
                box[nx][ny] = 1
                day[nx][ny] = day[x][y] + 1
                deq.append([nx,ny])

zeroflag = False
resultday = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            zeroflag = True

        if resultday < day[i][j]:
            resultday = day[i][j]

if zeroflag:
    print(-1)
else:
    print(resultday)
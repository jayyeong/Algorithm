import sys
from collections import deque
input = sys.stdin.readline
dz = [1, -1, 0, 0, 0, 0] # 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dy = [0, 0, 0, 0, -1, 1]
dx = [0, 0, -1, 1, 0, 0]

M, N, H = map(int,input().rstrip().split())

tomato_box = [[[] for _ in range(N)] for _ in range(H)] #z, y, x 좌표
day = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
tomato = deque()

for i in range(H):
    for j in range(N):
        tomato_box[i][j].extend([int(x) for x in input().rstrip().split()])
        for k in range(M):
            if tomato_box[i][j][k] == 1:
                tomato.append([i,j,k])

def bfs():

    while tomato:
        t = tomato.popleft()
        z, y, x = t[0], t[1], t[2]
        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if tomato_box[nz][ny][nx] == 0:
                    tomato_box[nz][ny][nx] = 1
                    day[nz][ny][nx] = day[z][y][x] + 1
                    tomato.append([nz,ny,nx])

bfs()
zeroflag = False
resultday = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato_box[i][j][k] == 0:
                zeroflag = True
            if resultday < day[i][j][k]:
                resultday = day[i][j][k]

if zeroflag:
    print(-1)
else:
    print(resultday)
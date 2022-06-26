import sys
N, M = map(int,input().split())
input = sys.stdin.readline
dx = [-1, 1, 0, 0] # 북, 남, 서, 동
dy = [0, 0, -1, 1]
paper = []
ans = 0

#   @@@@   @@
#          @@
#   @  @
#   @  @@  @@@
#   @@  @   @

for i in range(N):
    paper.append([int(x) for x in input().split()])

visited = [[0 for _ in range(M)] for _ in range(N)]

def dfs(x,y,n,c):
    global dfs_max
    if c == 4:
        if dfs_max < n:
            dfs_max = n
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dfs(nx,ny,n + paper[nx][ny],c + 1)
                    visited[nx][ny] = 0

def t_spin(x,y):
    t_max = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M: # +1칸
            nnx = nx + dx[i]
            nny = ny + dy[i]
            if 0 <= nnx < N and 0 <= nny < M: # +2칸
                    for h in [-1,1]: #볼록한 부분
                        value = paper[x][y]
                        if i == 0 or i == 1: #세로로 길면
                            sny = ny + h
                            if 0 <= sny < M:
                                value += paper[nx][ny]
                                value += paper[nnx][nny]
                                value += paper[nx][sny]
                        elif i == 2 or i == 3: #가로로 길면
                            snx = nx + h
                            if 0 <= snx < N:
                                value += paper[nx][ny]
                                value += paper[nnx][nny]
                                value += paper[snx][ny]
                        if t_max < value:
                            t_max = value
    return t_max

for i in range(N):
    for j in range(M):
        dfs_max = 0
        visited[i][j] = 1
        dfs(i,j,paper[i][j],1)
        visited[i][j] = 0
        block_max = max(dfs_max, t_spin(i, j))
        ans = max(ans,block_max)

print(ans)
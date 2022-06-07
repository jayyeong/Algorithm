import sys
N, M = map(int,input().split())
input = sys.stdin.readline
dx = [-1, 1, 0, 0] # 북, 남, 서, 동
dy = [0, 0, -1, 1]

#   @@@@   @@
#          @@
#   @  @
#   @  @@  @@@
#   @@  @   @

paper = []


for i in range(N):
    paper.append([int(x) for x in input().split()])

visited = [[0 for _ in range(M)] for _ in range(N)]

maxi = 0
def dfs(x,y,n,c):
    global maxi
    if c == 4:
        if maxi < n:
            maxi = n

    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    dfs(nx,ny,n + paper[nx][ny],c + 1)
                    visited[nx][ny] = 0

def t_spin(x,y,n):
    mm = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            nnx = nx + dx[i]
            nny = ny + dy[i]
            if 0 <= nnx < N and 0 <= nny < M:
                    for h in [-1,1]:
                        s = n
                        if i == 0 or i == 1:
                            sny = ny + h
                            if 0 <= sny < M:
                                s += paper[nx][ny]
                                s += paper[nnx][nny]
                                s += paper[nx][sny]
                        elif i == 2 or i == 3:
                            snx = nx + h
                            if 0 <= snx < N:
                                s += paper[nx][ny]
                                s += paper[nnx][nny]
                                s += paper[snx][ny]
                        if mm < s:
                            mm = s
    return mm


#dfs(0,0,paper[0][0],1)
#print(maxi)
#print(visited)

result = 0
for i in range(N):
    for j in range(M):
        maxi = 0
        visited[i][j] = 1
        dfs(i,j,paper[i][j],1)
        visited[i][j] = 0
        ma = max(maxi,t_spin(i,j,paper[i][j]))
        if result < ma:
            result = ma

print(result)
#각 자리에서 나올수 있는 최대값을 뽑기


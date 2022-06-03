from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

N, M = map(int,input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int,input())))
#print(maze) # 1 길,0 벽
visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs(x,y):
    que = deque()
    que.append([x,y])
    visited[x][y] = 1
    while que:
        a,b = que.popleft()
        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]
            if 0 <= nx < N and 0 <= ny <M:
                if visited[nx][ny] == 0 and maze[nx][ny] == 1:
                    visited[nx][ny] = visited[a][b] + 1
                    que.append([nx,ny])
bfs(0,0)
print(visited[N - 1][M - 1])
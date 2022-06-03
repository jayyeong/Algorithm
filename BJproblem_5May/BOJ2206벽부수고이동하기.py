from collections import deque
import sys
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
road = []

N, M = map(int,input().split())
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

for i in range(N):
    road.append(list(map(int,list(input().rstrip()))))

def bfs():
    que = deque()
    que.append([0,0,0])
    visited[0][0][0] = 1
    while que:
        x,y,z = que.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][z]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:

                if road[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    que.append([nx,ny,z])

                elif road[nx][ny] == 1 and z == 0:
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1
                    que.append([nx,ny,z + 1])

    return -1
print(bfs())
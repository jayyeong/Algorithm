from collections import deque
import sys

N, M = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
graph = []

for i in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

def bfs(a,b):
    count = 0
    deq = deque()
    visited[a][b] = True
    deq.append([a,b,0])

    while deq:
        x, y, c = deq.popleft()
        count = max(count,c)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 'L' and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    deq.append([nx,ny,c + 1])
    return count

result = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            if 0 < j < M - 1 and graph[i][j + 1] == 'L' and graph[i][j - 1] == 'L':
                continue
            if 0 < i < N - 1 and graph[i + 1][j] == 'L' and graph[i - 1][j] == 'L':
                continue
            visited = [[False] * M for _ in range(N)]
            result = max(result,bfs(i,j))
print(result)
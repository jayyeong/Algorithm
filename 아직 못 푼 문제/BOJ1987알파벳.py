from collections import deque
import sys
input = sys.stdin.readline
R, C = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
maze = []
for _ in range(R):
    maze.append(list(input().rstrip()))
maxi = 0
alphabet = [0 for i in range(26)] # A 65, Z 90
# print(alphabet[ord('Z') - 65])
def dfs(x,y,n):
    global maxi
    maxi = max(n,maxi)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            if alphabet[ord(maze[nx][ny]) - 65] == 0:
                alphabet[ord(maze[nx][ny]) - 65] = 1
                dfs(nx,ny,n + 1)
                alphabet[ord(maze[nx][ny]) - 65] = 0
alphabet[ord(maze[0][0]) - 65] = 1
dfs(0,0,1)
print(maxi)

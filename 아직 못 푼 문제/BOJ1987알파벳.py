import copy
import sys
input = sys.stdin.readline
R, C = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
maze = []
for _ in range(R):
    maze.append(list(input().rstrip()))
# print(maze)

box = []
box.append(maze[0][0])
ss = []

def dfs(x,y,arr: list):

    if x < 0 or x >= R or y < 0 or y >= C:
        return False

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and not maze[nx][ny] in arr:
            temp = copy.deepcopy(arr)
            temp.append(maze[nx][ny])
            dfs(nx,ny,temp)
    #print(arr)
    ss.append(len(arr))

dfs(0,0,box)
print(max(ss))
N, M = map(int,input().split())
road = []
wallList = []
for i in range(N):
    road.append(list(map(int,list(input()))))
    for j in range(M):
        if road[i][j] == 1:
            wallList.append([i,j])

def dfs(x,y,count):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if x == N - 1 and y == M - 1:
        return count

    if x < N - 1 and road[x + 1][y] == 0:
        dfs(x + 1,y,count + 1)
    elif x > 1 and road[x - 1][y] == 0:
        dfs(x - 1,y,count + 1)
    elif y < M - 1 and road[x][y + 1] == 0:
        dfs(x,y + 1,count + 1)
    elif y > 1 and road[x + 1][y] == 0:
        dfs(x,y - 1,count + 1)
    else:
        return False

print(dfs(0,0,0))
for wall in wallList:
    road[wall[0]][wall[1]] = 0

    road[wall[0]][wall[1]] = 1

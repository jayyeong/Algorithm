N, M = map(int,input().split())
road = []
wallList = []
for i in range(N):
    road.append(list(map(int,list(input()))))
    for j in range(M):
        if road[i][j] == 1:
            wallList.append([i,j])

def bfs(x,y):
    count = 0
    while 1:
        if x == N - 1 and y == M - 1:
            return count

        
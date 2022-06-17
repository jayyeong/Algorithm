import sys
sys.setrecursionlimit(10**6)
T = int(input())

def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if ground[x][y] == 1:
        ground[x][y] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

for _ in range(T):
    M, N, K = map(int,input().split())
    ground = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    for _ in range(K):
        col, row = map(int,sys.stdin.readline().rstrip().split())
        ground[row][col] = 1

    for i in range(N):
        for j in range(M):
            if dfs(i,j) == True:
                count += 1

    print(count)
N, M = map(int, input().split())

icebox = []
for i in range(N):
    icebox.append(list(map(int,list(str(input())))))
print(icebox)

def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if icebox[x][y] == 0:
        icebox[x][y] = 1
        dfs(x - 1,y)
        dfs(x + 1,y)
        dfs(x,y - 1)
        dfs(x,y + 1)
        return True
    return False

count = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            count += 1

print(icebox)
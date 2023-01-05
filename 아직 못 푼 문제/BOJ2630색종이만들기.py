import sys

sys.setrecursionlimit(10**6)

N = int(input())
count = 0
paper = []

for _ in range(N):
    paper.append([int(x) for x in sys.stdin.readline().split()])

#print(paper)

def dfs(x, y, n, color):
    global count
    flag = True

    if n == 1:
        if paper[x][y] == color:
            count += 1
        return

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != color:
                flag = False

    if flag == True:
        count += 1
        return

    else:
        k = n // 2
        dfs(x, y, k, color)
        dfs(x, y + k, k, color)
        dfs(x + k, y, k, color)
        dfs(x + k, y + k, k, color)

dfs(0,0,N, False)
print(count)
count = 0
dfs(0,0,N, True)
print(count)
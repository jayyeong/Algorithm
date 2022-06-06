import sys

N = int(input())
input = sys.stdin.readline

colorpaper = []
for _ in range(N):
    colorpaper.append([int(x) for x in input().split()])
#print(colorpaper)
count = 0
white = 0
def dfs(x, y, n):
    global count
    flag = True

    if n == 1:
        if colorpaper[x][y] == 1:
            count += 1
            return
        else:
            return
    for i in range(x,x + n):
        for j in range(y,y + n):
            if colorpaper[i][j] == 0:
                flag = False

    if flag == True:
        count += 1
        return
    else:
        s = n // 2
        dfs(x,y,s)
        dfs(x + s,y,s)
        dfs(x,y + s,s)
        dfs(x + s, y + s,s)

def w(x, y, n):
    global white
    flag = True

    if n == 1:
        if colorpaper[x][y] == 0:
            white += 1
            return
        else:
            return
    for i in range(x,x + n):
        for j in range(y,y + n):
            if colorpaper[i][j] == 1:
                flag = False

    if flag == True:
        white += 1
        return
    else:
        s = n // 2
        w(x,y,s)
        w(x + s,y,s)
        w(x,y + s,s)
        w(x + s, y + s,s)

dfs(0,0,N)
w(0,0,N)
print(white)
print(count)
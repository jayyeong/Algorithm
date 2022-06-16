import sys

N = int(input())
input = sys.stdin.readline
colorpaper = []

for _ in range(N):
    colorpaper.append([int(x) for x in input().split()])
blue = 0
white = 0

def Count(x, y, n):
    global blue, white
    flag = True
    check = colorpaper[x][y]

    for i in range(x,x + n):
        for j in range(y,y + n):
            if colorpaper[i][j] != check:
                flag = False

    if flag == True:
        if check == 1:
            blue += 1
        else:
            white += 1
    else:
        s = n // 2
        Count(x,y,s)
        Count(x + s,y,s)
        Count(x,y + s,s)
        Count(x + s, y + s,s)

Count(0,0,N)

print(white)
print(blue)
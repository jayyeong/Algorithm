import sys
N = int(input())
input = sys.stdin.readline
paper = []

for _ in range(N):
    paper.append([int(x) for x in input().split()])

minus_one_count = 0
zerocount = 0
one_count = 0

def zero(x,y,n):
    global zerocount
    flag = True
    if n == 1:
        if paper[x][y] == 0:
            zerocount += 1
            return
        else:
            return

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != 0:
                flag = False

    if flag == True:
        zerocount += 1
        return
    else:
        a = n // 3
        zero(x, y, a)
        zero(x, y + a, a)
        zero(x, y + 2 * a, a)
        zero(x + a, y, a)
        zero(x + a, y + a, a)
        zero(x + a, y + 2 * a, a)
        zero(x + 2 * a, y, a)
        zero(x + 2 * a, y + a, a)
        zero(x + 2 * a, y + 2 * a, a)

def minusone(x,y,n):
    global minus_one_count
    flag = True

    if n == 1:
        if paper[x][y] == -1:
            minus_one_count += 1
            return
        else:
            return

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != -1:
                flag = False

    if flag == True:
        minus_one_count += 1
        return
    else:
        a = n // 3
        minusone(x, y, a)
        minusone(x, y + a, a)
        minusone(x, y + 2 * a, a)
        minusone(x + a, y, a)
        minusone(x + a, y + a, a)
        minusone(x + a, y + 2 * a, a)
        minusone(x + 2 * a, y, a)
        minusone(x + 2 * a, y + a, a)
        minusone(x + 2 * a, y + 2 * a, a)

def one(x,y,n):
    global one_count
    flag = True

    if n == 1:
        if paper[x][y] == 1:
            one_count += 1
            return
        else:
            return

    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != 1:
                flag = False

    if flag == True:
        one_count += 1
        return
    else:
        a = n // 3
        one(x, y, a)
        one(x, y + a, a)
        one(x, y + 2 * a, a)
        one(x + a, y, a)
        one(x + a, y + a, a)
        one(x + a, y + 2 * a, a)
        one(x + 2 * a, y, a)
        one(x + 2 * a, y + a, a)
        one(x + 2 * a, y + 2 * a, a)

zero(0,0,N)
minusone(0,0,N)
one(0,0,N)

print(minus_one_count)
print(zerocount)
print(one_count)
import sys
N = int(input())
input = sys.stdin.readline
paper = []

for _ in range(N):
    paper.append([int(x) for x in input().split()])

minus_one_count = 0
zero_count = 0
one_count = 0

def Count(x,y,n):
    global minus_one_count, zero_count, one_count

    check = paper[x][y]
    flag = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != check:
                flag = False

    if flag == True:
        if check == -1:
            minus_one_count += 1
        elif check == 0:
            zero_count += 1
        elif check == 1:
            one_count += 1
    else:
        a = n // 3
        Count(x, y, a)
        Count(x, y + a, a)
        Count(x, y + 2 * a, a)
        Count(x + a, y, a)
        Count(x + a, y + a, a)
        Count(x + a, y + 2 * a, a)
        Count(x + 2 * a, y, a)
        Count(x + 2 * a, y + a, a)
        Count(x + 2 * a, y + 2 * a, a)

Count(0,0,N)

print(minus_one_count)
print(zero_count)
print(one_count)
import sys
sys.setrecursionlimit(10**6)
N, M = map(int,input().split())
r,c,di = map(int,input().split())
# 0 북, 1 동, 2 남, 3서
area = []
for _ in range(N):
    area.append([int(x) for x in input().split()])

def clean(x,y,d,count):
    if area[x][y] == 0:
        area[x][y] = 2

    if count == 4:
        #print("4번 실행")
        if d == 0:
            if area[x + 1][y] == 1:
                #print("종료")
                return
            else:
                clean(x + 1,y,0,0)

        elif d == 3:
            if area[x][y + 1] == 1:
                #print("종료")
                return
            else:
                clean(x,y + 1,3,0)

        elif d == 2:
            if area[x - 1][y] == 1:
                #print("종료")
                return
            else:
                clean(x - 1,y,2,0)

        elif d == 1:
            if area[x][y - 1] == 1:
                #print("종료")
                return
            else:
                clean(x,y - 1,1,0)

    if count <= 3:
        if d == 0:
            if area[x][y - 1] == 0:
                #print("서쪽으로 가서 청소")
                clean(x,y - 1,3,0)
            else:
                #print("서쪽으로 돌기")
                clean(x,y,3,count + 1)

        elif d == 3:
            if area[x + 1][y] == 0:
                #print("남쪽으로 가서 청소")
                clean(x + 1,y,2,0)
            else:
                #print("남쪽으로 돌기")
                clean(x,y,2,count + 1)

        elif d == 2:
            if area[x][y + 1] == 0:
                #print("동쪽으로 가서 청소")
                clean(x,y + 1,1,0)
            else:
                #print("동쪽으로 돌기")
                clean(x,y,1,count + 1)

        elif d == 1:
            if area[x - 1][y] == 0:
                #print("북쪽으로 가서 청소")
                clean(x - 1,y,0,0)
            else:
                #print("북쪽으로 돌기")
                clean(x,y,0,count + 1)

clean(r,c,di,0)
#print(area)
result = 0
for i in range(N):
    for j in range(M):
        if area[i][j] == 2:
            result += 1
print(result)
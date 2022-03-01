import copy
import sys
sys.setrecursionlimit(10**6)
N = int(input())
area = []
for i in range(N):
    area.append([int(x) for x in input().split()])

def dfs(x,y,k):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False

    if qq[x][y] >= k:
        qq[x][y] = 0
        dfs(x - 1,y,k)
        dfs(x + 1,y,k)
        dfs(x,y - 1,k)
        dfs(x,y + 1,k)
        return True
    return False


box= []
for a in range(1,101):
    count = 0
    qq = copy.deepcopy(area)
    for i in range(N):
        for j in range(N):
            if dfs(i,j,a) == True:
                count += 1
    box.append(count)
print(max(box))

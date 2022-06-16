from itertools import combinations
import sys
input = sys.stdin.readline

dosi = []
home = []
chicken = []
N, M = map(int, input().split())

for i in range(N):
    dosi.append([int(x) for x in input().split()])
    for j in range(N):
        if dosi[i][j] == 1:
            home.append([i,j])
        elif dosi[i][j] == 2:
            chicken.append([i,j])

# print(dosi)
# print(home)
# print(chicken)

def dosichicken():
    Slist = []
    for selectCk in combinations(chicken,M):
        S = 0
        #print(selectCk)
        for h in home:
            count = int(1e9)
            for c in selectCk:
                if count > abs(h[0] - c[0]) + abs(h[1] - c[1]):
                    count = abs(h[0] - c[0]) + abs(h[1] - c[1])
            S += count
        Slist.append(S)
    return min(Slist)

print(dosichicken())
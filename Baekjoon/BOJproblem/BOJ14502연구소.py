import sys
import copy
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

blank = [] # 빈공간 리스트
box = [] # 지도
virus = [] # 바이러스 위치 리스트
resultBox = []

# 입력
N, M = map(int, input().split())
for i in range(N):
    box.append([int(x) for x in input().split()])
    for j in range(M):
        if box[i][j] == 2:  # 바이러스 위치 저장
            virus.append([i,j])
        elif box[i][j] == 0:  # 빈공간, 벽이 들어 갈 수 있는 위치 저장
            blank.append([i,j])

def infection(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if B[x][y] == 1:
        return False

    if B[x][y] == 0 or B[x][y] == 2:
        B[x][y] = 3 # 바이러스 감염 3
        infection(x - 1, y)
        infection(x + 1, y)
        infection(x, y - 1)
        infection(x, y + 1)
        return True
    return False

for a in combinations(blank, 3):
    B = copy.deepcopy(box)
    for s in a:
        p = s[0]
        q = s[1]
        B[p][q] = 1  # 벽 세우기
    for v in virus:
        infection(v[0], v[1])

    result = 0
    for i in range(N):
        result += B[i].count(0)
    resultBox.append(result)

print(max(resultBox))




import sys
R, C, M = map(int, input().split())

shark_list = []
ans = 0

fishing_zone = [[0] * (C + 1) for _ in range(R + 1)]

for _ in range(M):
    shark_list.append([int(x) for x in sys.stdin.readline().rstrip().split()] + [1])
    # 위치 (row, col), 속력, 방향, 크기, 생존 유무 1 = 생, 0 = 죽

def shark_moving(shark):
    r, c, s, d, z, live = shark



for i in range(1, C + 1): # 낚시왕이 오른쪽으로 한칸 이동
    if i == 2:
        break
    nearest_shark = int(1e9)

    for s in shark_list:
        if s[1] == i and s[5] == 1:
            if nearest_shark > s[0]:
                nearest_shark = s[0]

    for s in shark_list: # 상어 잡기
        if s[0] == nearest_shark and s[5] == 1:
            s[5] = 0
            ans += s[4]
            break
    for s in shark_list:
        if s[5] == 1:
            shark_moving(s)


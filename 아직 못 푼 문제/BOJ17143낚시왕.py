import sys
R, C, M = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

shark_list = []
ans = 0

for _ in range(M):
    shark_list.append([int(x) for x in sys.stdin.readline().rstrip().split()] + [1])
    # 위치 (row, col), 속력, 방향, 크기, 생존 유무 1 = 생, 0 = 죽
    # 1 위, 2 아래, 3 오른쪽, 4 왼쪽

def shark_moving(shark):
    r, c, s, d, z, live = shark

    d -= 1

    while s > 0:
        nx, ny = r + dx[d], c + dy[d]

        if 1 <= nx <= R and 1 <= ny <= C:
            r, c = nx, ny
            s -= 1

        else:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
            continue

    return (r, c)





for i in range(1, C + 1): # 낚시왕이 오른쪽으로 한칸 이동

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

    print(ans)

    for i in range(len(shark_list)):
        if shark_list[i][5] == 1:
            x, y = shark_moving(shark_list[i])
            shark_list[i][0] = x
            shark_list[i][1] = y

    fishing_zone = [[] * (C + 1) for _ in range(R + 1)]

    print(fishing_zone)
    for s in shark_list:
        if s[5] == 1:
            fishing_zone[s[0]][s[1]].append(s)

    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if len(fishing_zone[i][j]) > 1:
                fishing_zone[i][j].sort(key= lambda x: x[4], reverse=True)
                for k in range(len(fishing_zone[i][j]) - 1):
                    fishing_zone[i][j][k][5] = 0

    print(ans)
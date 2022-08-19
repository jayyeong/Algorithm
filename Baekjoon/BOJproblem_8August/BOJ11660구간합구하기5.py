import sys
N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append([int(x) for x in sys.stdin.readline().rstrip().split()])

for i in range(N):
    for j in range(1, N):
        arr[i][j] += arr[i][j - 1]

for j in range(N):
    for i in range(1, N):
        arr[i][j] += arr[i - 1][j]

for _ in range(M):
    ans = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())

    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1 # 좌표 조정

    ans += arr[x2][y2]

    if x1 - 1 >= 0:
        ans -= arr[x1 - 1][y2]

    if y1 - 1 >= 0:
        ans -= arr[x2][y1 - 1]

    if x1 - 1 >= 0 and y1 - 1 >= 0:
        ans += arr[x1 - 1][y1 - 1]

    print(ans)
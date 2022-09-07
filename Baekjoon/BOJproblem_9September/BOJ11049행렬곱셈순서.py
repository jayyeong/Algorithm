import sys
N = int(input())
arr = []

INF = 2 ** 31
for _ in range(N):
    arr.append([int(x) for x in sys.stdin.readline().split()])

DP = [[0] * N for _ in range(N)]

for i in range(1, N):
    for j in range(N - i):
        end = i + j
        DP[j][end] = INF

        for k in range(j, end):
            DP[j][end] = min(DP[j][end], DP[j][k] + DP[k + 1][end] + arr[j][0] * arr[k][1] * arr[end][1])

print(DP[0][N - 1])

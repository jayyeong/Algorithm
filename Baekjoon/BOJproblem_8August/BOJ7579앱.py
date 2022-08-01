import sys

N, M = map(int,input().split())

app_memory = [0] + [int(x) for x in sys.stdin.readline().rstrip().split()]
app_deactive = [0] + [int(x) for x in sys.stdin.readline().rstrip().split()]

DP = [[0] * (sum(app_deactive) + 1) for i in range(N + 1)]

ans = int(1e9)

for i in range(1, N + 1):
    for j in range(1, sum(app_deactive) + 1):
        if app_deactive[i] <= j:
            DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - app_deactive[i]] + app_memory[i])
        else:
            DP[i][j] = DP[i - 1][j]

        if DP[i][j] >= M:
            ans = min(ans, j)

print(ans)
import sys
N = int(input())
rgb = []
for _ in range(N):
    rgb.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * 3 for _ in range(N + 1)]
dp[0] = rgb[0]

for i in range(1, N - 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2]

print(min(dp[N - 1]))
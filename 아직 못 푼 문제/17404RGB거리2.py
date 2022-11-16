import sys
N = int(input())
rgb = []
for _ in range(N):
    rgb.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * 3 for _ in range(N + 1)]
min_list = []
for k in range(3):

    dp[0] = [1000 * 1000] * 3
    dp[0][k] = rgb[0][k]

    for i in range(1, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + rgb[i][2]

    dp[N - 1][k] = 1000 * 1000
    min_list.extend(dp[N - 1])

print(min(min_list))
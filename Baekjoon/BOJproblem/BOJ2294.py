import sys
n, k = map(int,input().split())
coins = []
dp = [-1 for x in range(10001)]
for _ in range(n):
    x = int(sys.stdin.readline())
    if x <= 10000:
        coins.append(x)
coins.sort()

for coin in coins:
    if coin <= 10000:
        dp[coin] = 1

for i in range(1,k+1):
    for coin in coins:
        if dp[i - coin] != -1:
            if dp[i] == -1:
                dp[i] = dp[i - coin] + 1
            else:
                dp[i] = min(dp[i],dp[i - coin] + 1)

print(dp[k])
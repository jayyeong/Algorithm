N, M = map(int, input().split())

coin = []

for i in range(N):
    coin.append(int(input()))

DP = [10001] * (M + 1)
DP[0] = 0

for c in coin:
    for i in range(c, M + 1):
        DP[i] = min(DP[i - c] + 1, DP[i])

print(DP)
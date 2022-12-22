N, K = map(int, input().split())

Coins = []
count = 0

for _ in range(N):
    Coins.append(int(input()))

for i in range(N - 1, -1, -1):
    if K - Coins[i] >= 0:
        count += K // Coins[i]
        K %= Coins[i]

print(count)
N = int(input())
warehouse = [int(x) for x in input().split()]

DP = [0] * (N + 1)
DP[0] = warehouse[0]
DP[1] = max(warehouse[1], warehouse[0])

for i in range(2, N):
    DP[i] = max(DP[i - 1], DP[i - 2] + warehouse[i])

print(DP)
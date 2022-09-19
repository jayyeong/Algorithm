N = int(input())
DP = [0] * (31)

DP[2] = 3
DP[4] = 11

for i in range(6, N + 1, 2):
    for j in range(4, i, 2):
        DP[i] += DP[i - j] * 2
    DP[i] += DP[i - 2] * DP[2]
    DP[i] += 2
print(DP[N])
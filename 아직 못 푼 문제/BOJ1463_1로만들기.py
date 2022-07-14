N = int(input())
DP = [[0] for _ in range(N + 1)]
for i in range(2, N + 1):
    if i % 2 == 0 and i % 3 != 0:
        DP[i][0] = min(DP[i // 2] + 1, DP[i - 1] + 1)

    elif i % 3 == 0 and i % 2 != 0:
        DP[i] = min(DP[i // 3] + 1, DP[i - 1] + 1)

    elif i % 3 == 0 and i % 2 == 0:
        DP[i] = min(DP[i // 2] + 1, DP[i // 3] + 1, DP[i - 1] + 1)

    else:
        DP[i] = DP[i - 1] + 1
print(DP[N])
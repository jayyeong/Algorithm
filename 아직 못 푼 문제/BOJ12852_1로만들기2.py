N = int(input())
DP = [[0,[]] for _ in range(N + 1)]

DP[1][1].append(1)

for i in range(2, N + 1):
    DP[i][0] = DP[i - 1][0] + 1
    DP[i][1] = DP[i - 1][1] + [i]

    if i % 3 == 0:
        if DP[i // 3][0] + 1 < DP[i][0]:
            DP[i][0] = DP[i // 3][0] + 1
            DP[i][1] = DP[i // 3][1] + [i]

    if i % 2 == 0:
        if DP[i // 2][0] + 1 < DP[i][0]:
            DP[i][0] = DP[i // 2][0] + 1
            DP[i][1] = DP[i // 2][1] + [i]

print(DP[N][0])
print(' '.join(map(str, reversed(DP[N][1]))))
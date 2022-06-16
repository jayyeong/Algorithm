N = int(input())

DP = [[0 for x in range(10)] for _ in range(N)]

for i in range(1,10):
    DP[0][i] = 1

for i in range(1,N):
    for j in range(10):
        if j == 0:
            DP[i][j + 1] += DP[i - 1][j]
        elif j == 9:
            DP[i][j - 1] += DP[i - 1][j]
        else:
            DP[i][j + 1] += DP[i - 1][j]
            DP[i][j - 1] += DP[i - 1][j]

print(sum(DP[N - 1]) % 1000000000)

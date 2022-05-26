N = int(input())
health = [int(x) for x in input().split()]
happy = [int(x) for x in input().split()]

HP = 100
MIND = 0

DP = [[0 for _ in range(100)] for _ in range(N + 1)]

for i in range(1,N + 1):
    for j in range(1,100):
        if health[i - 1] <= j:
            DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - health[i - 1]] + happy[i - 1])
        else:
            DP[i][j] = DP[i - 1][j]

print(DP[N][99])
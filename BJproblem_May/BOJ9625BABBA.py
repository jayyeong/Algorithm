K = int(input())
DP = [0 for _ in range(46)]
DP[1] = 1
DP[2] = 1

for i in range(3,K + 1):
    DP[i] = DP[i - 2] + DP[i - 1]

print(DP[K - 1],DP[K])

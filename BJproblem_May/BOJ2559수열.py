N, K = map(int,input().split())
arr = [int(x) for x in input().split()]

DP = [0]
max_value = -1000000
for i in range(N):
    DP.append(DP[i] + arr[i])
#print(DP)

for i in range(N - K + 1):
    if max_value < DP[i + K] - DP[i]:
        max_value = DP[i + K] - DP[i]
print(max_value)
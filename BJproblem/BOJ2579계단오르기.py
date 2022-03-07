import sys
N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

DP = []

DP.append(stairs[0])
if N >= 2:
    DP.append(stairs[0] + stairs[1])
if N >= 3:
    DP.append(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
for i in range(3,N):
    DP.append(max(DP[i - 3] + stairs[i - 1] + stairs[i],DP[i - 2] + stairs[i]))

print(DP[N - 1])
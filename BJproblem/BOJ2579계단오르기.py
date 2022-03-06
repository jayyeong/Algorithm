import sys
N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))

count = 0
DP = [0] * 9
for i in range(N):
    if count == 2:
        DP[i] = max()
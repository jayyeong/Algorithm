N = int(input())

DP = [0] * (N + 1)

DP[1] = 0

x = 1

while DP[N] == 0:

a = [x * 5, x * 3, x * 2, x + 1]
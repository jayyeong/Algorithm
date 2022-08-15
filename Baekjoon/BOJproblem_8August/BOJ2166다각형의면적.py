import sys

N = int(input())

poly = []

for _ in range(N):
    poly.append([int(x) for x in input().split()])

poly.append(poly[0])

ans = 0
for i in range(len(poly) - 1):
    ans += poly[i][0] * poly[i + 1][1] - poly[i][1] * poly[i + 1][0]

print(format(abs(ans)/2, ".1f"))
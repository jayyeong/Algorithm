import sys
input = sys.stdin.readline
n = int(input())
tri = []
for _ in range(n):
    tri.append([int(x) for x in input().split()])
for i in range(1,n):
    tri[i][0] += tri[i - 1][0]
    for j in range(1,i):
        tri[i][j] += max(tri[i - 1][j - 1],tri[i - 1][j])
    tri[i][i] += tri[i - 1][i - 1]
print(max(tri[n - 1]))
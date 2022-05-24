import sys
input = sys.stdin.readline
N, M = map(int,input().split())

arr = [int(x) for x in input().split()]
box = [0] * (N + 1)

for i in range(N):
    box[i + 1] = box[i] + arr[i]

for _ in range(M):
    x, y = map(int,input().split())
    print(box[y] - box[x - 1])
def dfs():
    if len(arr) == N//2:
        return sum(arr)
    for i in range(N):


N = int(input())

box = []

for _ in range(N):
    box.append([int(x) for x in input().split()])

arr = []
import sys
from collections import deque
import copy

input = sys.stdin.readline

N, M, K = map(int,input().split())

A = []
for _ in range(N):
    A.append([int(x) for x in input().split()])

tree = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x,y,z = map(int,input().split())
    tree[x - 1][y - 1].append(z)

food = [] # 양분
for _ in range(N):
    food.append([5 for x in range(N)])


for _ in range(K):
    for t in tree:
        if t[2] <= food[t[0]][t[1]] and t[2] > 0:
            food[t[0]][t[1]] -= t[2]
            t[2] += 1
        else:
            t[2] = -t[2]

    for t in tree:
        if t[2] < 0:
            food[t[0]][t[1]] += -t[2] // 2
            t[2] = 0

    for t in list(tree):
        if t[2] % 5 == 0 and t[2] > 0:
            if t[0] > 0 and t[1] > 0:
                tree.appendleft([t[0] - 1, t[1] - 1, 1])
            if t[0] > 0:
                tree.appendleft([t[0] - 1, t[1], 1])
            if t[0] > 0 and t[1] < N - 1:
                tree.appendleft([t[0] - 1, t[1] + 1, 1])
            if t[1] > 0:
                tree.appendleft([t[0], t[1] - 1, 1])
            if t[1] < N - 1:
                tree.appendleft([t[0], t[1] + 1, 1])
            if t[0] < N - 1 and t[1] > 0:
                tree.appendleft([t[0] + 1, t[1] - 1, 1])
            if t[0] < N - 1:
                tree.appendleft([t[0] + 1, t[1], 1])
            if t[0] < N - 1 and t[1] < N - 1:
                tree.appendleft([t[0] + 1, t[1] + 1, 1])

    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]

#print(tree)
count = 0
for t in tree:
    if t[2] > 0:
        count += 1
print(count)
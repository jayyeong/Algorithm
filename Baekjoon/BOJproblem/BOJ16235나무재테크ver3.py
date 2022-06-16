import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int,input().split())

A = []
for _ in range(N):
    A.append([int(x) for x in input().split()])

tree = [[deque() for _ in range(N)] for _ in range(N)]
deadtree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x,y,z = map(int,input().split())
    tree[x - 1][y - 1].append(z)

food = [] # 양분
for _ in range(N):
    food.append([5 for x in range(N)])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] > food[i][j]:
                    for _ in range(k, len(tree[i][j])):
                        deadtree[i][j].append(tree[i][j].pop())
                    break
                else:
                    food[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1

    for i in range(N):
        for j in range(N):
            while deadtree[i][j]:
                food[i][j] += deadtree[i][j].pop() // 2


    for i in range(N):
        for j in range(N):
            for k in range(len(tree[i][j])):
                if tree[i][j][k] % 5 == 0 and tree[i][j][k] > 0:
                    for l in range(8):
                        nx, ny, = i + dx[l], j + dy[l]

                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue
                        tree[nx][ny].appendleft(1)

            food[i][j] += A[i][j]

#print(tree)
count = 0
for i in range(N):
    for j in range(N):
        count += len(tree[i][j])
print(count)
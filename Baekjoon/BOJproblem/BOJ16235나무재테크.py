import sys
input = sys.stdin.readline

N, M, K = map(int,input().split())
A = []
for _ in range(N):
    A.append([int(x) for x in input().split()])

tree = [] # 나무

for _ in range(M):
    x,y,z = map(int,input().split())
    tree.append([x - 1,y - 1,z])

tree.sort(key=lambda x: (x[0],x[1],x[2]))
food = [] # 양분
for _ in range(N):
    food.append([5 for x in range(N)])

def spring():
    tree.sort(key=lambda x: (x[0], x[1], x[2]))
    for i in range(len(tree)):
        if tree[i][2] <= food[tree[i][0]][tree[i][1]] and tree[i][2] > 0:
            food[tree[i][0]][tree[i][1]] -= tree[i][2]
            tree[i][2] += 1
        else:
            tree[i][2] = -tree[i][2]

def summmer():
    for t in tree:
        if t[2] < 0:
            food[t[0]][t[1]] += -t[2] // 2
            t[2] = 0

def fall():
    for t in tree:
        if t[2] % 5 == 0 and t[2] > 0:
            if t[0] > 0 and t[1] > 0:
                tree.append([t[0] - 1, t[1] - 1, 1])
            if t[0] > 0:
                tree.append([t[0] - 1, t[1], 1])
            if t[0] > 0 and t[1] < N - 1:
                tree.append([t[0] - 1, t[1] + 1, 1])
            if t[1] > 0:
                tree.append([t[0], t[1] - 1, 1])
            if t[1] < N - 1:
                tree.append([t[0], t[1] + 1, 1])
            if t[0] < N - 1 and t[1] > 0:
                tree.append([t[0] + 1, t[1] - 1, 1])
            if t[0] < N - 1:
                tree.append([t[0] + 1, t[1], 1])
            if t[0] < N - 1 and t[1] < N - 1:
                tree.append([t[0] + 1, t[1] + 1, 1])

def winter():
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]

for _ in range(K):
    spring()
    summmer()
    fall()
    winter()

print(tree)
count = 0
for t in tree:
    if t[2] > 0:
        count += 1
print(count)
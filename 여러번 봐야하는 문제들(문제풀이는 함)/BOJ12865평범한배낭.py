N, K = map(int,input().split())
item = []

pack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    item.append([int(x) for x in input().split()])

for i in range(1,N + 1):
    for j in range(1,K + 1):
        if item[i - 1][0] <= j:
            pack[i][j] = max(pack[i - 1][j], pack[i - 1][j - item[i - 1][0]] + item[i - 1][1])
        else:
            pack[i][j] = pack[i - 1][j]

print(pack[N][K])
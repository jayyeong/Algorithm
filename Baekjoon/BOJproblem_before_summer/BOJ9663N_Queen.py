def Nq(x):
    if x == N:
        return 1
    for i in range(N):
        for j in range(N):
            box[i][j] = 1

N = int(input())
box = [[0] * N] * N


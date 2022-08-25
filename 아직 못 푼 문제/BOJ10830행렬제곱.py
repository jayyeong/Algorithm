import sys

N, R = map(int, sys.stdin.readline().split())

matrix = []

for _ in range(N):
    matrix.append([int(x) for x in sys.stdin.readline().split()])

def power_matrix(mat, r):

    if r == 1:
        for i in range(N):
            for j in range(N):
                mat[i][j] %= 1000
        return mat

    tmp = power_matrix(mat, r//2)

    if r % 2 == 1:
        return mul(mul(tmp, tmp, N), mat, N)
    else:
        return mul(tmp, tmp, N)

def mul(A, B, n):

    Z = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            x = 0
            for i in range(n):
                x += A[row][i] * B[i][col]
            Z[row][col] = x % 1000

    return Z

ans = power_matrix(matrix, R)

for a in ans:
    print(' '.join(map(str, a)))
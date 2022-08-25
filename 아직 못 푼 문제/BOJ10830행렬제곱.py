import sys

N, R = map(int, sys.stdin.readline().split())

matrix = []

for _ in range(N):
    matrix.append([int(x) for x in sys.stdin.readline().split()])

def power_matrix(mat, n):

    if n == 1:
        for i in range(n):
            for j in range(n):
                mat[i][j] %= 1000
        return mat

    tmp = power_matrix(mat, n//2)

    if n % 2 == 1:
        return mul(mul(tmp, tmp, n), mat, n)
    else:
        return mul(tmp, tmp, n)

def mul(A, B, n):
    print(A, B)
    Z = [[0] * n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            x = 0
            for i in range(n):
                x += A[row][i] * B[i][col]
            Z[row][col] = x % 1000

    return Z

print(power_matrix(matrix, R))
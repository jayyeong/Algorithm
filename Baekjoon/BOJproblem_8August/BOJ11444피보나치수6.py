import sys

constant = 1000000007

fibo = [[1], [0]]
matrix = [[1, 1], [1, 0]]

def power_matrix(mat, r):

    if r == 1:
        for i in range(2):
            for j in range(2):
                mat[i][j] %= constant
        return mat

    tmp = power_matrix(mat, r//2)

    if r % 2 == 1:
        return mul(mul(tmp, tmp), mat)
    else:
        return mul(tmp, tmp)

def mul(A, B):

    Z = [[0] * 2 for _ in range(2)]

    for row in range(2):
        for col in range(2):
            x = 0
            for i in range(2):
                x += A[row][i] * B[i][col]
            Z[row][col] = x % constant

    return Z

N = int(input())


ans = power_matrix(matrix, N)

print(ans[1][0])
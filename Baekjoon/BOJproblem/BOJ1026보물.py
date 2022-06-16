N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

A.sort()
B.sort(reverse=True)
S = 0
for i in range(N):
    S += A[i]*B[i]

print(S)
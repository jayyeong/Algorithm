N = int(input())
A = [int(x) for x in input().split()]
M = int(input())
B = [int(x) for x in input().split()]
A.sort()
for b in B:
    print(A.count(b),end=' ')


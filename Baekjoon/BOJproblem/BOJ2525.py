A, B = map(int,input().split())
C = int(input())

D = (B + C) % 60
E = (B + C) // 60

if A + E >= 24:
    A = A + E - 24
else:
    A = A + E

print(A,D)
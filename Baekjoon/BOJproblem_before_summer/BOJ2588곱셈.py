A = int(input())
B = int(input())

c = B % 10
d = B % 100 - c
e = B - d - c

print(A*c)
print(A*(d//10))
print(A*(e//100))
print(A*B)
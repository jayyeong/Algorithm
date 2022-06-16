a, b = input().split()
A = list(a)
B = list(b)
ar = list(reversed(A))
br = list(reversed(B))

x = ''
y = ''

for i in ar:
    x += i
for i in br:
    y += i

if int(x) > int(y):
    print(int(x))
else:
    print(int(y))
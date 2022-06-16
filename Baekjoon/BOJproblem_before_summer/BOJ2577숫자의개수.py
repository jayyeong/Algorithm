A = int(input())
B = int(input())
C = int(input())
D = A*B*C
a = list(str(D))

box = [0 for i in range(10)]
for i in a:
    box[int(i)] += 1

for i in box:
    print(i)
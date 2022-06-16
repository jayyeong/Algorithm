def solve(n: int):
    sum = n
    nlist = list(str(n))
    for i in nlist:
        sum += int(i)
    return sum

box = []
for i in range(10001):
    box.append(0)

for i in range(1,10001):
    if solve(i) < 10001:
        box[solve(i)] = 1

for i in range(1,10001):
    if box[i] == 0:
        print(i)

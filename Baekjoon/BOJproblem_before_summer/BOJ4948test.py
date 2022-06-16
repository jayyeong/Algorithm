N = int(input())

box = [x for x in range(1,N + 1)]
nbox = [x for x in range(N,2*N + 1)]

for x in box:
    for y in box:
        if y != x and y % x == 0:
            box.remove(y)

for i in box:
    for j in nbox:
        if j % i == 0:
            nbox.remove(j)

print(nbox)
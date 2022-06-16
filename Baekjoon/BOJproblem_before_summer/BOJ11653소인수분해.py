N = int(input())
box = []
i = 2
if N != 1:
    while N != 1:
        if N % i == 0:
            box.append(i)
            N = N // i
            i = 2
        else:
            i += 1
for x in box:
    print(x)
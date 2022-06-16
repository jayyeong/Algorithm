N = int(input())

for i in range(N):
    box = list(input())
    count = 0
    a = 0
    for k in box:
        if k == 'O':
            a += 1
            count += a
        else:
            a = 0
    print(count)
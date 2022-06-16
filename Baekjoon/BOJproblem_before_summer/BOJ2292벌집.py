N = int(input())

x = 2
y = 7
count = 2

if N == 1:
    print(1)
else:
    while 1:
        if x <= N and y >= N:
            print(count)
            break
        else:
            x += 6*(count - 1)
            y += 6*count
            count += 1

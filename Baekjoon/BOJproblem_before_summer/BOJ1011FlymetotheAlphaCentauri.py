T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    l = b - a
    x = 3
    y = 4
    count = 3

    z = 2
    if l == 1 or l == 2:
        print(l)
    else:
        while 1:
            if l >= x and l <= y:
                print(count)
                break
            else:
                if count % 2 == 0:
                    x -= 1
                x += z
                y += z
                count += 1
                if count % 2 == 0:
                    z += 1



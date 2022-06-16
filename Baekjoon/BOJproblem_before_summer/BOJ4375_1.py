ones = 1

while 1:
    try:
        n = int(input())
    except EOFError:
        break
    ones = 1
    while 1:
        if ones % n == 0:
            print(len(str(ones)))
            break
        else:
            ones = ones * 10 + 1

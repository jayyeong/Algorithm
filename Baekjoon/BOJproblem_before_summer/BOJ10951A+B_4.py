while 1:
    try:
        x, y = input().split()
    except ValueError:
        break
    except EOFError:
        break
    print(int(x) + int(y))


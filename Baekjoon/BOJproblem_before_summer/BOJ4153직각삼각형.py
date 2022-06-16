while 1:
    box = [int(x) for x in input().split()]
    box.sort()

    if box[0] == 0:
        break
    if box[0]**2 + box[1]**2 == box[2]**2:
        print("right")
    else:
        print("wrong")


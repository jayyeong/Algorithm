import math
T = int(input())

for _ in range(T):
    box = [int(x) for x in input().split()]
    di = math.sqrt((box[0] - box[3])**2+(box[1] - box[4])**2)
    m = 0
    n = 0
    if box[2] <= box[5]:
        m = box[5]
        n = box[2]
    else:
        m = box[2]
        n = box[5]

    if di == 0 and box[2] == box[5]:
        print(-1)
        continue

    if di >= m:
        if box[2] + box[5] == di:
            print(1)
        elif box[2] + box[5] < di:
            print(0)
        else:
            print(2)
    else:
        if m - n == di:
            print(1)
        elif m - n < di:
            print(2)
        else:
            print(0)
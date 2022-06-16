N = int(input())

for i in range(N):
    box = [int(x) for x in input().split()]
    M = sum(box[1:])/box[0]
    count = 0
    for j in range(1, box[0] + 1):
        if box[j] > M:
            count += 1
    print("%.3f"%((count/box[0])*100),"%",sep='')
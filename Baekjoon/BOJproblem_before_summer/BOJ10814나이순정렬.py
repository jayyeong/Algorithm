N = int(input())
box = []

for i in range(N):
    box.append(input().split())
    box[i][0] = int(box[i][0])
    box[i].append(i)

box.sort()
box.sort(key = lambda x : (x[0],x[2]))

for x in box:
    print(x[0], x[1])
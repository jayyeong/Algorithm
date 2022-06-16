N = int(input())
box = []

for _ in range(N):
    box.append([int(x) for x in input().split()])

box.sort(key = lambda x:(x[1],x[0]))

for i in box:
    print(i[0], i[1])
N = int(input())
box = []

for _ in range(N):
    box.append([int(x) for x in input().split()])

box.sort()
for i in box:
    print(i[0], i[1])

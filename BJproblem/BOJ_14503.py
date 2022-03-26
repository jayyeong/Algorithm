N, M = map(int, input().split())
r, c, d= map(int, input().split())

box = []
for _ in range(N):
    box.append([int(x) for x in input().split()])

print(box)


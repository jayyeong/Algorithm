N, M, B = map(int,input().split())
block = []
for _ in range(N):
    block.append([int(x) for x in input().split()])
print(block)


for i in range(257):

    for x in range(N):
        for y in range(M):

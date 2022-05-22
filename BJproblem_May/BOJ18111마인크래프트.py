N, M, B = map(int,input().split())
block = []
for _ in range(N):
    block.append([int(x) for x in input().split()])
print(block)

MaxLevel = (sum(block) + B) // (N * M)
print((sum(block) + B) // (N * M))

for i in range(MaxLevel):
    for x in range(N):
        for y in range(M):
            if block[x][y] < i:
                
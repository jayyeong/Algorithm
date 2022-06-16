N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))

rope.sort()
DP = []
for i in range(N):
    DP.append(rope[i]*(N - i))

print(max(DP))
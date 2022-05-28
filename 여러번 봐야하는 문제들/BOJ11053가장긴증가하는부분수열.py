N = int(input())
box = [int(x) for x in input().split()]
DP = []

DP.append(1)

for i in range(1, N):
    r = []
    for j in range(i):
        if box[j] < box[i]:
            r.append(DP[j])
    if len(r) == 0:
        DP.append(1)
    else:
        DP.append(max(r) + 1)
print(DP)
print(max(DP))
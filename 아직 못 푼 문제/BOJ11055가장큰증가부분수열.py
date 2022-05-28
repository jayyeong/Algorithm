N = int(input())
Arr = [int(x) for x in input().split()]

DP = [0 for _ in range(N)]
DP[0] = Arr[0]

for i in range(N):
    box = []
    count = 0
    for j in range(i):
        if Arr[j] < Arr[i]:
            box.append(DP[j])
    if len(box) == 0:
        DP[i] = Arr[i]
    else:
        DP[i] = max(box) + Arr[i]
print(max(DP))
N = int(input())
Arr = [int(x) for x in input().split()]

DP = [0 for _ in range(N)]
DP2 = [0 for _ in range(N)]
DP[0] = 1

for i in range(1,N):
    box = []
    for j in range(i):
        if Arr[j] < Arr[i]:
            box.append(DP[j])
        if len(box) == 0:
            DP[i] = 1
        else:
            DP[i] = max(box) + 1
    box2 = []
    for k in range(N - 1,N - i - 1,-1):
        if Arr[k] < Arr[N - i - 1]:
            box2.append(DP2[k])
        if len(box2) == 0:
            DP2[N - i - 1] = 0
        else:
            DP2[N - i - 1] = max(box2) + 1
result = -1000
for i in range(N):
    if result < DP[i] + DP2[i]:
        result = DP[i] + DP2[i]

# print(DP)
# print(DP2)
print(result)

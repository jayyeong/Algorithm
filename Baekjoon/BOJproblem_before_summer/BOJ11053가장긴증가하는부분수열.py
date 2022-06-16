N = int(input())
box = [int(x) for x in input().split()]
arr = []

arr.append(1)

c = 0

for i in range(1, N):
    r = []
    for j in range(i):
        if box[j] < box[i]:
            r.append(arr[j])
    if len(r) == 0:
        arr.append(1)
    else:
        arr.append(max(r) + 1)

print(max(arr))


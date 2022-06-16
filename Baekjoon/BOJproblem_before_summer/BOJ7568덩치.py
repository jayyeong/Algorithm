N = int(input())
box = []

for _ in range(N):
    box.append([int(x) for x in input().split()])

arr = [1 for x in range(N)]
for i in range(N):
    for j in range(i):
        if box[j][0] < box[i][0] and box[j][1] < box[i][1]:
            arr[j] += 1
        if box[j][0] > box[i][0] and box[j][1] > box[i][1]:
            arr[i] += 1

for x in arr:
    print(x,end=' ')
print()
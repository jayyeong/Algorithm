N, M = map(int,input().split())
trees = [int(x) for x in input().split()]

start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for t in trees:
        if t - mid > 0:
            count += t - mid
    if count >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
import sys
input = sys.stdin.readline

K, N = map(int,input().split())
lenson = []
for _ in range(K):
    lenson.append(int(input()))

start, end = 1, max(lenson)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for son in lenson:
        count += son // mid
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)
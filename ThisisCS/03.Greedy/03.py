N,M = map(int,input().split())
arr = []
for _ in range(N):
    box = [int(x) for x in input().split()]
    arr.append(min(box))

print(max(arr))



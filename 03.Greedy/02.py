N, M, K = map(int,input().split())
box = [int(x) for x in input().split()]
box.sort(reverse=True)
print(box)
count = 0
S = 0
for _ in range(M):
    if count == K:
        S += box[1]
        count = 0
    else:
        S += box[0]
        count += 1
print(S)
N, M = map(int,input().split())
box = [int(x) for x in input().split()]
solve = 0

for i in range(N):
    for j in range(i + 1,N):
        for k in range(j + 1,N):
            if solve <= box[i] + box[j] + box[k] <= M:
                solve = box[i] + box[j] + box[k]
print(solve)
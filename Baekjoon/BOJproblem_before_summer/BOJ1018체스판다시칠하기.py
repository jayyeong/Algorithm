def start_BW(x :list):
    count = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if x[i][j] != 'B':
                    count += 1
            else:
                if x[i][j] != 'W':
                    count += 1

    return count

def start_WB(x :list):
    count = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if x[i][j] != 'W':
                    count += 1
            else:
                if x[i][j] != 'B':
                    count += 1

    return count

N, M = map(int,input().split())
box = []
slist = []
for _ in range(N):
    box.append(list(input()))
for i in range(N - 7):
    for j in range(M - 7):
        arr = [row[j:j+8] for row in box[i:i+8]]
        slist.append(min(start_BW(arr),start_WB(arr)))

print(min(slist))
N = int(input())
box =[]

for i in range(15):
    box.append([0 for j in range(14)])

for i in range(14):
    box[0][i] = i + 1

for i in range(1,15):
    for j in range(14):
        box[i][j] = box[i - 1][j] + box[i][j - 1]

for x in range(N):
    k = int(input())
    n = int(input())
    print(box[k][n - 1])


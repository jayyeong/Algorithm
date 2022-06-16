T = int(input())

box = [[0 for _ in range(2)] for _ in range(41)]


box[0][0] = 1
box[1][1] = 1

for i in range(2,len(box)):
    box[i][0] = box[i - 1][0] + box[i - 2][0]
    box[i][1] = box[i - 1][1] + box[i - 2][1]

for _ in range(T):
    N = int(input())
    print(box[N][0],box[N][1])

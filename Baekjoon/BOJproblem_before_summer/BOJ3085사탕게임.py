def ch(arr):
    mlist = []
    ulist = []
    for i in range(N):
        c = 0
        x = arr[i][0]
        for j in range(N):
            if arr[i][j] == x:
                c += 1
                mlist.append(c)
            else:
                x = arr[i][j]
                c = 1
                mlist.append(c)
    #가로줄 체크

    for i in range(N):
        c = 0
        x = arr[0][i]
        for j in range(N):
            if arr[j][i] == x:
                c += 1
                mlist.append(c)
            else:
                x = arr[j][i]
                c = 1
                mlist.append(c)
    #세로줄 체크
    return max(mlist)

box = []
maxlist = []
M = 0

N = int(input())
for i in range(N):
    box.append(list(input()))

temp = 'a'

# 가로줄 바꾸기

for i in range(N):
    for j in range(N - 1):
        temp = box[i][j]
        box[i][j] = box[i][j + 1]
        box[i][j + 1] = temp
        maxlist.append(ch(box))
        temp = box[i][j]
        box[i][j] = box[i][j + 1]
        box[i][j + 1] = temp

for i in range(N):
    for j in range(N - 1):
        temp = box[j][i]
        box[j][i] = box[j + 1][i]
        box[j + 1][i] = temp
        maxlist.append(ch(box))
        temp = box[j][i]
        box[j][i] = box[j + 1][i]
        box[j + 1][i] = temp

print(max(maxlist))
# 바꾸기 기능만 추가하면 끝

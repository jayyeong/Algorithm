box = []
for i in range(9):
    box.append(int(input()))

M = 0
num = 0
for i in range(9):
    if box[i] > M:
        M = box[i]
        num = i + 1

print(M)
print(num)
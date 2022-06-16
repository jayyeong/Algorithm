box = []
for i in range(9):
    box.append(int(input()))

#print(box)

sum = 0
x = 0
y = 0

for i in range(9):
    sum += box[i]

#print(sum)

for i in range(9):
    for j in range(i):
        if sum - box[i] - box[j] == 100:
            x = i
            y = j
            #print(sum - box[i] - box[j])

del box[x]
del box[y]

box.sort()

for i in box:
    print(i)
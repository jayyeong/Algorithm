box = []
for _ in range(3):
    box.append([int(x) for x in input().split()])

if box[0][0] == box[1][0]:
    a = box[2][0]
elif box[1][0] == box[2][0]:
    a = box[0][0]
else:
    a = box[1][0]

if box[0][1] == box[1][1]:
    b = box[2][1]
elif box[1][1] == box[2][1]:
    b = box[0][1]
else:
    b = box[1][1]

print(a,b)



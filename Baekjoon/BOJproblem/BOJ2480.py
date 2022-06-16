box = list(map(int,input().split()))
box.sort()
count = 0
if box[0] == box[1]:
    if box[0] == box[2]:
        count = max(box) * 1000 + 10000
    else:
        count = box[0] * 100 + 1000
elif box[1] == box[2]:
    if box[1] == box[0]:
        count = max(box) * 1000 + 10000
    else:
        count = box[1] * 100 + 1000
elif box[0] == box[2]:
    if box[0] == box[1]:
        count = max(box) * 1000 + 10000
    else:
        count = box[0] * 100 + 1000
else:
    count = max(box) * 100
print(count)
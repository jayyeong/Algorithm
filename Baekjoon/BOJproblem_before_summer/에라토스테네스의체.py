box = [x for x in range(1, 123456*2+1)]

box.remove(1)

for x in box:
    for y in box:
        if y != x and y % x == 0:
            box.remove(y)
print(len(box))
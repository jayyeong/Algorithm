box = []
checkbox = []
for i in range(10):
    x = int(input())
    box.append(x % 42)

checkbox.append(box[0])

flag = 0
for i in range(10):
    for j in checkbox:
        if box[i] != j:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        checkbox.append(box[i])

print(len(checkbox))

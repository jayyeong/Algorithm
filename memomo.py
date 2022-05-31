Arr = [2,3]

def test(arr: list):
    box = arr.copy()
    if box[- 1] == 1:
        return box
    box.append(1)
    return test(box)

print(test(Arr))
print(Arr)


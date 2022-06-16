N = int(input())
count = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            box = []
            box.extend(list(str(h)))
            box.extend(list(str(m)))
            box.extend(list(str(s)))
            print(box)
            if '3' in box:
                count += 1
print(count)
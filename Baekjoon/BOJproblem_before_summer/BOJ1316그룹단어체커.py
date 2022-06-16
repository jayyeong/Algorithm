N = int(input())
count = N
for i in range(N):
    box = list(input())
    ch = [0 for i in range(26)]
    x = box[0]
    for j in range(len(box)):
        if ch[ord(box[j]) - 97] == 0: # 최초
            ch[ord(box[j]) - 97] = 1
            x = box[j]
        elif box[j] == x: #연속
            continue
        else:
            count -= 1
            break
print(count)


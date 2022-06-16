S = list(input())
box = []

for i in range(26):
    box.append(-1)

for i in range(len(S)):
    if box[ord(S[i]) - 97] == -1:
        box[ord(S[i]) - 97] = i

for i in box:
    print(i,end=' ')

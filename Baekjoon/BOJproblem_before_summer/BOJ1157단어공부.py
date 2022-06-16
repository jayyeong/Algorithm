s = list(input().lower())
box = []
for i in range(26):
    box.append(0)

for i in range(len(s)):
    box[ord(s[i]) - 97] += 1

M = max(box)
count = 0
for i in range(26):
    if box[i] == M:
        count += 1

if count == 1:
    print(chr(box.index(M) + 97).upper())
elif count >= 2:
    print("?")
N = int(input())
box = [int(x) for x in input().split()]
nbox = []
M = 0
for i in box:
    if M < i:
        M = i

for i in box:
    nbox.append((i/M)*100)

print(sum(nbox)/N)
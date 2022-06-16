N = int(input())

x = 2
y = 3
count = 2

if N == 1:
    count = 1
else:
    while 1:
        if x <= N and y >= N:
            break
        else:
            x += count
            y += count + 1
            count += 1

if count % 2 == 1:
    l = count
    r = 1
else:
    l = 1
    r = count

for i in range(x,N):
    if count % 2 == 1:
        l -= 1
        r += 1
    else:
        l += 1
        r -= 1

print(l,r,sep='/')
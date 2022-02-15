N = int(input())
A = list(input().split(' '))
x,y = 1,1

for a in A:
    if a == 'U' and x > 1:
        x -= 1
    elif a == 'D' and x < N:
        x += 1
    elif a == 'R' and y < N:
        y += 1
    elif a == 'L' and y > 1:
        y -= 1
print(x,y)
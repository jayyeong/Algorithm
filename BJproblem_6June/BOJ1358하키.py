W, H, X, Y, P = map(int,input().split())

Plist = []

r = H//2
leftx = X
lefty = Y + r

rightx = X + W
righty = Y + r

leftside = pow(r**2-lefty**2,0.5) - leftx

count = 0
for _ in range(P):
    x,y = map(int,input().split())
    if Y <= y <= Y + H:
        leftside = leftx - pow(r**2-(y - lefty)**2,0.5)
        rightside = rightx + pow(r**2-(y - righty)**2,0.5)
        #print(leftside,rightside,x,y)
        if leftside <= x <= rightside:
            count += 1

print(count)

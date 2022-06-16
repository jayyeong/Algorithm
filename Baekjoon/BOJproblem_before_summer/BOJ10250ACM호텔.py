T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    w = N // H
    h = N % H
    if h == 0:
        h = H
        w -= 1

    box = ""
    if w < 9 :
        box += str(h)
        box += str(0)
        box += str(w + 1)
        print(box)
    else:
        print(str(h) + str(w + 1))
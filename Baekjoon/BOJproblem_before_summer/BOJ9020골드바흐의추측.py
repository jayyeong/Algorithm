def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if(x % i == 0):
            return False
    return True

alist = list(range(2, 10000))
m = []
for i in alist:
    if is_prime(i):
        m.append(i)

N = int(input())
for _ in range(N):
    x = int(input())
    a = []
    q = 0
    w = 0
    for j in m:
        y = x - j
        if y < 0:
            break
        if y in m and y >= j:
            a.append([j, y])
    mi = a[0][1] - a[0][0]
    for s in range(len(a)):
        if mi >= a[s][1] - a[s][0]:
            q = a[s][0]
            w = a[s][1]
    print(q, w)
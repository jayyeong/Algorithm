def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if(x % i == 0):
            return False
    return True

alist = list(range(2,246912))
m = []
for i in alist:
    if is_prime(i):
        m.append(i)

while 1:
    x = int(input())
    if x == 0:
        break
    cnt = 0
    for i in m:
        if x < i <= 2*x:
            cnt += 1
    print(cnt)

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if(x % i == 0):
            return False
    return True

T = int(input())

for _ in range(T):
    n = int(input())
    a = n // 2
    b = a
    while 1:
        if is_prime(a) and is_prime(b):
            print(a,b)
            break
        a -= 1
        b += 1
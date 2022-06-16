def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i*i <= x:
        if(x % i == 0):
            return False
        i += 1

    return True

def main():
    M = int(input())
    N = int(input())
    box = []
    for i in range(M,N + 1):
        if(is_prime(i)):
            box.append(i)
    if len(box) == 0:
        print(-1)
    else:
        print(sum(box))
        print(min(box))

main()
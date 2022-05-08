def factorial(x):
    n = 1
    for i in range(1,x + 1):
        n = n * i
    return n

N, M = map(int,input().split())

print(factorial(N)//(factorial(N - M)*factorial(M)))
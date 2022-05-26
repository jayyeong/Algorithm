N = int(input())
for i in range(1,N + 1):
    for _ in range(((2*N - 1) - (2*i - 1))//2):
        print(' ',end='')
    for _ in range(2*i - 1):
        print('*',end='')
    if i != N:
        print()
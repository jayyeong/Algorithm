N = int(input())
for i in range(N,0,-1):
    for _ in range(((2*N - 1) - (2*i - 1))//2):
        print(' ',end='')
    for _ in range(2*i - 1):
        print('*',end='')
    print()
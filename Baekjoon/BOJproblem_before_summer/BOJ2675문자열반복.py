N = int(input())

for i in range(N):
    R, s = input().split()
    S = list(s)
    for i in S:
        print(i*int(R),end='')
    print()
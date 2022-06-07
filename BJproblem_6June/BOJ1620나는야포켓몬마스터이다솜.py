import sys
input = sys.stdin.readline

N, M = map(int,input().rstrip('\n').split())

dogam = []
for i in range(N):
    dogam.append(input().rstrip('\n'))

for i in range(M):
    q = input().rstrip('\n')
    if 65 <= ord(q[0]) <= 90:
        print(dogam.index(q) + 1)
    else:
        print(dogam[int(q) - 1])
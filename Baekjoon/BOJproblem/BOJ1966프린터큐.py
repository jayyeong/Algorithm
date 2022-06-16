import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    arr = [int(x) for x in input().split()]
    B = []
    for i in range(len(arr)):
        B.append([arr[i],i])
    #print(B)

    x = -1
    count = 0
    while x != M:
        if arr[0] < max(arr):
            arr.append(arr[0])
            B.append(B[0])
            del arr[0]
            del B[0]
        else:
            count += 1
            x = B[0][1]
            del arr[0]
            del B[0]
    print(count)
def Bsearch(arr,v,low,high):
    if low > high:
        return 0
    mid = (low+high) // 2
    if arr[mid] < v:
        return Bsearch(A,b,mid + 1,high)
    elif arr[mid] > v:
        return Bsearch(A,b,low,mid - 1)
    else:
        return 1
N = int(input())
A = [int(x) for x in input().split()]
M = int(input())
B = [int(x) for x in input().split()]


A.sort()
for b in B:
    print(Bsearch(A,b,0,N - 1),end=' ')
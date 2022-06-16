def Bsearch(arr,v,low,high):
    if low > high:
        return 0
    mid = (low+high) // 2
    if  arr[mid] > v:
        return Bsearch(arr,v,low,mid - 1)
    elif arr[mid] < v:
        return Bsearch(arr,v,mid + 1,high)
    else:
        return 1


N = int(input())
A = [int(x) for x in input().split()]
M = int(input())
B = [int(x) for x in input().split()]

A.sort() #오름차순으로 정렬
#print(A)
for b in B:
    print(Bsearch(A,b,0,len(A) - 1))




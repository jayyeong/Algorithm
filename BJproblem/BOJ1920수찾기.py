N = int(input())
A = [int(x) for x in input().split()]
M = int(input())
B = [int(x) for x in input().split()]

A.sort() #오름차순으로 정렬
print(A)
for b in B:
    if b in A:
        print(1)
    else:
        print(0)

def Bsearch(arr,v,low,high):
    if low > high:
        return False
    mid = (low+high)/2

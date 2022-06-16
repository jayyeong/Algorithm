N = int(input())
arr = set(int(x) for x in input().split())
q = list(arr)

q.sort()
for a in q:
    print(a,end=' ')
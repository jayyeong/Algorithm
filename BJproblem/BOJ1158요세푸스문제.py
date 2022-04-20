N, K = map(int,input().split())
arr = [x for x in range(1, N + 1)]
#print(arr)
i = 0
q = []

while arr:
    i = (i + (K - 1)) % len(arr)
    q.append(str(arr.pop(i)))

'''
print("<",end='')
for a in q:
    if a == q[-1]:
        print(a,end='')
    else:
        print(a,',',' ',sep='',end='')

print(">",end='')
'''

print("<%s>" %(', '.join(q)))


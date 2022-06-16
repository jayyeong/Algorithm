N = int(input())

box = [int(x) for x in input().split()]
a = []
for i in range(N):
    a.append([box[i]])
    a[i].append(i)

a.sort(key = lambda x:x[0])

q = 0
a[0].append(0)
for i in range(1,N):
    if a[i - 1][0] < a[i][0]:
        q += 1
        a[i].append(q)
    else:
        a[i].append(q)

a.sort(key = lambda x:x[1])
for x in a:
    print(x[2],end=' ')
print()

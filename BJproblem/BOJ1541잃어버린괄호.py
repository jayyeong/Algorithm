s = input()
#print(s)
a = s.split(sep='-')
#print(a_int)
arr = []
for q in a:
    bb = q.split(sep='+')
    n = 0
    for b in list(map(int,bb)):
        n += b
    arr.append(n)
#print(tree)
result = arr[0]
for i in range(1,len(arr)):
    result -= arr[i]
print(result)
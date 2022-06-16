def sq(n,arr):
    s = []
    if n == 3:
        return arr
    else:
        for i in arr:
            s.append(i*3)
        for i in arr:
            s.append(i+' '*len(arr)+i)
        for i in arr:
            s.append(i*3)
        return sq(n//3,s)

N = int(input())
star = ["***","* *","***"]
a = sq(N, star)
print(a)
for i in a:
    print(i)





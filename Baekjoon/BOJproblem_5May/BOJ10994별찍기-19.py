N = int(input())

Arr = ['*']

def square(n,arr: list):
    if n == N + 1:
        return arr
    box = []
    box.append('*'*((n - 1)*4 + 1))
    box.append('*'+' '*((n - 1)*4 - 1)+'*')
    for s in arr:
        box.append('* '+s+' *')
    box.append('*'+' '*((n - 1)*4 - 1)+'*')
    box.append('*'*((n - 1)*4 + 1))
    return square(n + 1,box)

if N == 1:
    result = Arr
else:
    result = square(2,Arr)
for i in result:
    print(i)
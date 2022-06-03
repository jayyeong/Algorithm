N = int(input())

Arr = [['*'],['*****','*    ','* ***','* * *','* * *','*   *','*****']]

def maze(n,arr: list):
    box = []
    if n == N + 1:
        return arr
    else:
        box.append('*'*(5 + 4*(n - 2)))
        box.append('*'+' '*(4 + 4*(n - 2)))
        for i in range(len(arr)):
            if i == 0:
                box.append('* '+arr[i]+'**')
            else:
                box.append('* '+arr[i]+' *')
        box.append('*'+' '*(3 + 4*(n - 2))+'*')
        box.append('*'*(5 + 4*(n - 2)))
        return maze(n + 1,box)
if N <= 2:
    result = Arr[N - 1]
else:
    result = maze(3,Arr[1])
# print(result)
for s in result:
    print(s.rstrip())
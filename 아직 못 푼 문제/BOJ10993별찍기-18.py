N = int(input())

starbox =[['*'],['*****',' *** ','  *  ']]
heightbox = [1 for _ in range(11)]
for i in range(2,11):
    heightbox[i] = heightbox[i - 1]*2 + 1

# print(heightbox)
def making(n,arr: list):
    box = []

    if n == N + 1:
        return arr

    elif n % 2 == 1:
        for i in range(heightbox[n - 1]):
            if i == 0:
                box.append(' '*(heightbox[n] - 1)+'*'+' '*(heightbox[n] - 1))
            else:
                box.append(' '*(heightbox[n] - 1 - i)+'*'+' '*(2*i - 1)+'*'+' '*(heightbox[n] - 1 - i))
        for i in range(heightbox[n - 1]):
            box.append(' '*(heightbox[n - 1] - i)+'*'+' '*i+arr[i]+' '*i+'*'+' '*(heightbox[n - 1] - i))
        box.append('*'*(heightbox[n - 1]*4+1))
        return making(n+1,box)

    else:
        box.append('*'*(heightbox[n - 1]*4+1))
        for i in range(heightbox[n - 1]):
            box.append(' ' * (i + 1) + '*' + ' ' * (heightbox[n - 1] - 1 - i) + arr[i] + ' '*(heightbox[n - 1] - 1 - i) + '*' + ' ' * (i + 1))
        for i in range(heightbox[n - 1] - 1,-1,-1):
            if i == 0:
                box.append(' '*(heightbox[n] - 1)+'*'+' '*(heightbox[n] - 1))
            else:
                box.append(' '*(heightbox[n] - 1 - i)+'*'+' '*(2*i - 1)+'*'+' '*(heightbox[n] - 1 - i))
        return making(n+1,box)

if N <= 2:
    x = starbox[N - 1]
else:
    x = making(3,starbox[1])
# print(x)
for s in x:
    print(s.rstrip())



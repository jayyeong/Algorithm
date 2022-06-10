N = int(input())

def flip(x,y,arr):
    k = y + 1 - x
    for i in range(k//2):
        temp = -arr[x - 1 + i]
        arr[x - 1 + i] = -arr[y - 1 - i]
        arr[y - 1 - i] = temp
#normal = [int(x) for x in range(1,N + 1)]

def one_check(arr):
    minuslist = []
    straight = True

    for a in arr:
        if a < 0:
            minuslist.append(a)

    if len(minuslist) == 1:
        return True


    for i in range(1,len(minuslist)):
        if minuslist[i] - minuslist[i - 1] != 1:
            straight = False

    if straight:
        return True
    return False

for _ in range(5):
    Fish = [int(x) for x in input().split()]
    if one_check(Fish):
        print('one')
        pass
    else:
        print('noone')
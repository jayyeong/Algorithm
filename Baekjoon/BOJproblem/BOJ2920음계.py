arr = [int(x) for x in input().split()]

ASC = [1,2,3,4,5,6,7,8]
DESC = [8,7,6,5,4,3,2,1]

if arr == ASC:
    print('ascending')
elif arr == DESC:
    print('descending')
else:
    print('mixed')
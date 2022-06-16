N = int(input())
sign = [x for x in input().split()]
#print(sign)

minnum = [0]
maxnum = [9]
last_st = 0
last_bt = 0
for i in range(N):
    c = 9
    if sign[i] == '>':
        last_bt = i + 1
        maxnum.append(8 - i)
    else:
        s = 8 - i
        maxnum.append(c)
        for j in range(last_bt,len(maxnum)):
            maxnum[j] = s
            s += 1
    #print(maxnum)
print(''.join(list(map(str, maxnum))))

for i in range(N):
    c = 0
    if sign[i] == '<':
        last_st = i + 1
        minnum.append(i + 1)
    else:
        s = i + 1
        minnum.append(c)
        for j in range(last_st, len(minnum)):
            minnum[j] = s
            s -= 1

    #print(minnum)
#print(minnum)
print(''.join(list(map(str, minnum))))

def solve(a: list):
    if len(a) <= 2:
        return 1
    c = int(a[0]) - int(a[1])
    flag = 0
    for i in range(len(a) - 1):
        if int(a[i]) - int(a[i + 1]) == c:
            flag = 1
        else:
            flag = 0
    if flag == 1:
        return 1
    elif flag == 0:
        return 0


N = int(input())
count = 0
for i in range(1,N + 1):
    s = list(str(i))
    if solve(s) == 1:
        count += 1
print(count)
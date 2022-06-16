s = input()
solve = 0
for i in range(1,int(s)):
    a = i
    nlist = list(str(i))
    for x in nlist:
        a += int(x)
    if a == int(s):
        solve = i
        break
print(solve)
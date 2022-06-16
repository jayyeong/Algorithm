N = int(input())
c = 0
x = 666
while c != N:
    s = list(str(x))
    s.reverse()

    for i in range(2, len(s)):
        if s[i - 2] == '6' and s[i - 1] == '6' and s[i] == '6':
            c += 1
            break
    x += 1
print(x - 1)
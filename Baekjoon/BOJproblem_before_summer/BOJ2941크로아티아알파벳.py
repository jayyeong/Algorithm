s = list(input())
count = len(s)
for i in range(len(s)):
    if s[i] == '=':
        if s[i - 1] == 'c':
            count -= 1
        elif s[i - 1] == 's':
            count -= 1
        elif s[i - 1] == 'z':
            if s[i - 2] == 'd':
                count -= 2
            else:
                count -= 1
    elif s[i] == '-':
        if s[i - 1] == 'c':
            count -= 1
        elif s[i - 1] == 'd':
            count -= 1
    elif s[i] == 'j':
        if s[i - 1] == 'l':
            count -= 1
        elif s[i - 1] == 'n':
            count -= 1
print(count)

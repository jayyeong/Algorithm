S = int(input())
a = 0
i = 1
count = 0
while S > 0:

    S -= i
    if S < 0:
        break
    i += 1
    count += 1

print(count)
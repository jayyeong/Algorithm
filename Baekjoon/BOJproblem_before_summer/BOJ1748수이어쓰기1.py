N = int(input())
count = 0

for i in range(2, int(len(str(N))) + 1):
    count += 9*(10**(i - 2))*(i - 1)


count += (N - (10**(int(len(str(N))) - 1) - 1)) * int(len(str(N)))

print(count)
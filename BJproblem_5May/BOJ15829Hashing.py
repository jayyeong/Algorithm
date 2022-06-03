L = int(input())
line = input()
count = 0
for i in range(len(line)):
    count += ((ord(line[i]) - 96)*(31**(i)))
print(count % 1234567891)
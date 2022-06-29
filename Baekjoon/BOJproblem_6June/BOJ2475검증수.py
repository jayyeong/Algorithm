import sys

numbers = [int(x) for x in sys.stdin.readline().rstrip().split()]

result = 0
for n in numbers:
    result += n**2

print(result%10)
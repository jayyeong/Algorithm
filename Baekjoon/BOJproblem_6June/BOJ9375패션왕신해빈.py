import sys

T = int(input())

for _ in range(T):
    cloth = {}
    result = 1
    n = int(input())
    for _ in range(n):
        name, type = sys.stdin.readline().rstrip().split()

        if not type in cloth:
            cloth[type] = 1
        else:
            cloth[type] += 1

    for i in cloth:
        result *= (cloth[i] + 1)

    print(result - 1)
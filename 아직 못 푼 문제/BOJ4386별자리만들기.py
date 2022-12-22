import sys
n = int(input())

stars = []

for _ in range(n):
    stars.append(list(map(float, sys.stdin.readline().split())))

print(stars)
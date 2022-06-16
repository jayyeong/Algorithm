N = int(input())

box = [int(x) for x in input().split()]

print(max(box)*min(box))
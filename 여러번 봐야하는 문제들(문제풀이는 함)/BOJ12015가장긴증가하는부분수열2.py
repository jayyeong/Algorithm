import sys
input = sys.stdin.readline

N = int(input())
Arr = [int(x) for x in input().split()]
box = [0]

for s in Arr:
    if box[-1] < s:
        box.append(s)
    else:
        left = 0
        right = len(box)
        while left < right:
            mid = (right+left)//2
            if box[mid]<s:
                left = mid + 1
            else:
                right = mid
        box[right] = s
print(len(box) - 1)
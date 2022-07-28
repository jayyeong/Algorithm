import sys
N, S = map(int, input().split())
array = [int(x) for x in sys.stdin.readline().rstrip().split()]

left = 0
right = 0
length = 100000
temp_sum = array[0]

while left <= right:
    if temp_sum >= S:
        length = min(length, right - left + 1)
        temp_sum -= array[left]
        left += 1
    else:
        right += 1
        if right < N:
            temp_sum += array[right]
        else:
            break

if length == 100000:
    print(0)
else:
    print(length)
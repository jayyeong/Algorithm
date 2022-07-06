import sys, copy
N = int(input())

max_arr = [int(x) for x in sys.stdin.readline().rstrip().split()]
min_arr = copy.copy(max_arr)

max_temp = copy.copy(max_arr)
min_temp = copy.copy(max_arr)

for _ in range(N - 1):
    b1, b2, b3 = map(int, sys.stdin.readline().rstrip().split())

    max_arr[0] = b1 + max(max_temp[0], max_temp[1])
    max_arr[1] = b2 + max(max_temp[0], max_temp[1], max_temp[2])
    max_arr[2] = b3 + max(max_temp[1], max_temp[2])

    min_arr[0] = b1 + min(min_temp[0], min_temp[1])
    min_arr[1] = b2 + min(min_temp[0], min_temp[1], min_temp[2])
    min_arr[2] = b3 + min(min_temp[1], min_temp[2])

    max_temp = copy.copy(max_arr)
    min_temp = copy.copy(min_arr)

print(max(max_arr), min(min_arr))
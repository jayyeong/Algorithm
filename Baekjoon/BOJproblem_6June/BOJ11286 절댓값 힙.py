import heapq
import sys
input = sys.stdin.readline

arr = []
N = int(input().rstrip())

for _ in range(N):
    x = int(input().rstrip())

    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr,(abs(x),x))
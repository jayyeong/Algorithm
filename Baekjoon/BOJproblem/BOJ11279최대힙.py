import heapq
import sys
N = int(input())
box = []
for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(box) == 0:
            print(0)
        else:
            print(heapq.heappop(box)[1])
    elif x > 0:
        heapq.heappush(box,(-x,x))
    
import heapq
import sys

max_heap = []
min_heap = []
input = sys.stdin.readline
N = int(input().rstrip())

for i in range(N):
    x = int(input().rstrip())
    if i % 2 == 0:
        heapq.heappush(max_heap,-x)
    else:
        heapq.heappush(min_heap,x)

    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        maxh_value = -heapq.heappop(max_heap)
        minh_value = heapq.heappop(min_heap)

        heapq.heappush(max_heap,-minh_value)
        heapq.heappush(min_heap,maxh_value)

    print(-max_heap[0])
import sys, heapq

N = int(input())
max_heap = []
min_heap = []

for i in range(N):
    x = int(sys.stdin.readline().rstrip())

    if i % 2 == 0:
        heapq.heappush(max_heap,-x)
    else:
        heapq.heappush(min_heap,x)

    if min_heap and max_heap and -max_heap[0] > min_heap[0]:
        max_n = -heapq.heappop(max_heap)
        min_n = heapq.heappop(min_heap)
        heapq.heappush(max_heap,-min_n)
        heapq.heappush(min_heap,max_n)

    print(-max_heap[0])
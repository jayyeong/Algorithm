from collections import deque
import heapq
import sys

N, M = map(int, input().split())

in_degree = [0 for _ in range(N + 1)]
problem_adj_list = [[] for i in range(N + 1)]
deq = []
toposort = []

for i in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    problem_adj_list[x].append(y)
    in_degree[y] += 1

for i in range(1,N + 1):
    if in_degree[i] == 0:
        heapq.heappush(deq, i)

while deq:
    node = heapq.heappop(deq)
    print(node, end = ' ')
    for p in problem_adj_list[node]:
        in_degree[p] -= 1
        if in_degree[p] == 0:
            heapq.heappush(deq, p)
print()
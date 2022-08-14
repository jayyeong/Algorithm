import sys
R, C, K = map(int, input().split())

graph = []
for _ in range(R):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))


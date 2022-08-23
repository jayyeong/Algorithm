import sys
TC = int(input())

for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())

    roads = []
    wormholes = []

    for _ in range(M):
        roads.append([int(x) for x in sys.stdin.readline().split()])

    for _ in range(W):
        wormholes.append([int(x) for x in sys.stdin.readline().split()])

    print(roads)
    print(wormholes)
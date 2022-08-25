import sys
TC = int(input())
INF = int(1e9)

def bellman(st):
    dis = [INF] * (N + 1)
    dis[st] = 0

    for i in range(N):
        for road in roads:
            now = road[0]
            next = road[1]
            cost = road[2]

            if dis[next] > cost + dis[now]:
                dis[next] = cost + dis[now]

                if i == N - 1:
                    return True

for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())

    roads = []

    for _ in range(M):
        s, e, t = map(int, sys.stdin.readline().split())
        roads.append([s, e, t])
        roads.append([e, s, t])

    for _ in range(W):
        s, e, t = map(int, sys.stdin.readline().split())
        roads.append([s, e, -t])

    ans = bellman(1)

    if ans:
        print('YES')
    else:
        print('NO')
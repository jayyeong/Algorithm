from collections import deque
import sys

input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
    N, K = map(int,input().rstrip().split())

    D = [0]
    D.extend([int(x) for x in input().rstrip().split()]) # n번째 건물 건설 시간
    in_degree = [0 for _ in range(N + 1)] # n번째 node 진입 차수
    adj_list_out = [[] for i in range(N + 1)] # n번째 노드에서 out인 노드 저장
    adj_list_in = [[] for i in range(N + 1)]  # n번째 노드에서 in인 노드 저장
    deq = deque()
    toposort = []
    Dtime = [0 for i in range(N + 1)] # n번째 건설까지 소요되는 시간

    for i in range(K):
        x, y = map(int,input().rstrip().split())
        adj_list_out[x].append(y)
        adj_list_in[y].append(x)
        in_degree[y] += 1
    W = int(input())

    for i in range(1,N + 1):
        if in_degree[i] == 0:
            deq.append(i)
            Dtime[i] = D[i] #

    while deq:
        node = deq.popleft()
        toposort.append(node)
        for s in adj_list_out[node]:
            in_degree[s] -= 1
            Dtime[s] = max(Dtime[s],Dtime[node] + D[s]) #
            if in_degree[s] == 0:
                deq.append(s)

    # for i in toposort:
    #     count = 0
    #     for b in adj_list_in[i]:
    #         if count < Dtime[b]:
    #             count = Dtime[b]
    #     Dtime[i] = D[i] + count

    print(Dtime[W])
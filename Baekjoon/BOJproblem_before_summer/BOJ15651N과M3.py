def dfs():
    if len(box) == M:
        print(" ".join(map(str,box)))
        return
    for i in range(1,N + 1):
        visit[i] = True
        box.append(i)
        dfs()
        box.pop()
        visit[i] = False

N, M = map(int, input().split())

box = []
visit = [False] * (N + 1)
dfs()


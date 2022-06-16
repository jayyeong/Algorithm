def check(arr):
    flag = 1
    for i in range(1,len(arr)):
        if arr[i - 1] > arr[i]:
            flag = 0
    if flag:
        return True
    else:
        return False

def dfs():
    if len(box) == M:
        if check(box):
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


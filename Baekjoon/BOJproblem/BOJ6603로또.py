import sys
input = sys.stdin.readline

def dfs(dep):
    if len(box) == 6:
        print(" ".join(map(str,box)))
        return
    for i in range(dep,t):
        box.append(Arr[i])
        dfs(i + 1)
        box.pop()


t = -1

while t != 0:
    arr = [int(x) for x in input().split()]
    t = arr[0]
    Arr = arr[1:]

    box = []
    dfs(0)
    print()

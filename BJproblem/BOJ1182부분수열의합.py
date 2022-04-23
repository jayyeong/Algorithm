def dfs(start,s):
    global count
    if start == N:
        return

    s += arr[start]

    if s == S:
        count += 1

    dfs(start + 1,s)
    dfs(start + 1,s - arr[start])




N, S = map(int,input().split())
arr = [int(x) for x in input().split()]

count = 0
q = []
dfs(0, 0)
print(count)
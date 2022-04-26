def dfs(x,y):
    global block
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if arr[x][y] == 1:
        block += 1
        arr[x][y] = 0

        dfs(x + 1,y)
        dfs(x - 1,y)
        dfs(x,y + 1)
        dfs(x,y - 1)
        return True
    return False

N = int(input())

arr = []
box = []
for _ in range(N):
    arr.append(list(map(int,list(input()))))
count = 0
for i in range(N):
    for j in range(N):
        block = 0
        if dfs(i,j):
            count += 1
            if block:
                box.append(block)
box.sort()
print(count)
for b in box:
    print(b)
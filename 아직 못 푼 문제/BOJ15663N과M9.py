N, M = map(int, input().split())
numbers = [int(x) for x in input().split()]
numbers.sort()

box = []
line = []
visited = [False] * (N + 1)

def dfs(depth):
    if depth == M:
        tmp = ' '.join(map(str, line))
        if tmp not in box:
            box.append(tmp)
        return

    for i in range(len(numbers)):
        if visited[i] == False:
            visited[i] = True
            line.append(numbers[i])
            dfs(depth + 1)
            line.pop()
            visited[i] = False

dfs(0)
for i in box:
    print(i)
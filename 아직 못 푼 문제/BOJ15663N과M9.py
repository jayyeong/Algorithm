N, M = map(int, input().split())

numbers = [int(x) for x in input().split()]
numbers.sort()


def dfs(depth, line):
    if depth == M:
        print(" ".join(str, line))

    for i in range(N):
        line.append(numbers[i])
        dfs(depth + 1, )

arr = []
dfs(0, arr)
N = int(input())
count = 0
row = [0] * N

def isgood(a):
        for i in range(a):
            if row[a] == row[i] or abs(row[a] - row[i]) == abs(a - i):
                return 0
        return 1

def dfs(n):
    global count
    if n == N:
        count += 1

    else:
        for i in range(N):
            row[n] = i
            if isgood(n):
                dfs(n + 1)

dfs(0)
print(count)


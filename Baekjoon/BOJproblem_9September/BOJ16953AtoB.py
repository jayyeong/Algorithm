from collections import deque
A, B = map(int, input().split())

def bfs(x):
    deq = deque()
    deq.append([x, 0])

    while deq:
        n, count = deq.popleft()

        if n == B:
            print(count + 1)
            exit(0)

        if int(str(n) + '1') <= 10**9:
            deq.append([int(str(n) + '1'), count + 1])

        if n * 2 <= 10**9:
            deq.append([n * 2, count + 1])

    print(-1)

bfs(A)
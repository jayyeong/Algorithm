from collections import deque
import sys

queue = deque()

N = int(input())

for _ in range(N):
    S = sys.stdin.readline().split()
    #print(S)
    if S[0] == 'push':
        queue.append(S[1])

    elif S[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())

    elif S[0] == 'size':
        print(len(queue))

    elif S[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif S[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif S[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
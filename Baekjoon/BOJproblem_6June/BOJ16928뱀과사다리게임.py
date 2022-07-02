import sys
from collections import deque

def bfs():
    deq = deque()
    deq.append([1, 0])
    visited[1] = True

    while deq:
        po, count = deq.popleft()

        if po == 100:
            print(count)
            break

        for i in range(1,7):
            newpo = po + i
            if newpo > 100:
                continue

            for k in range(len(sadari)):
                if newpo == sadari[k][0] and not visited[newpo]:
                    visited[newpo] = True
                    deq.append([sadari[k][1], count + 1])

            for j in range(len(baaam)):
                if newpo == baaam[j][0] and not visited[newpo]:
                    visited[newpo] = True
                    deq.append([baaam[j][1], count + 1])

            if not visited[newpo]:
                visited[newpo] = True
                deq.append([newpo, count + 1])

if __name__ == '__main__':
    N, M = map(int, input().split())
    visited = [False for _ in range(101)]
    sadari = []
    baaam = []

    for i in range(N):
        sadari.append([int(x) for x in sys.stdin.readline().rstrip().split()])
    for i in range(M):
        baaam.append([int(x) for x in sys.stdin.readline().rstrip().split()])

    bfs()
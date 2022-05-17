from collections import deque

deq = deque()
N, K = map(int,input().split())
arr = []
for i in range(1,N + 1):
    deq.append(i)

count = 1
while deq:
    if count % K == 0:
        arr.append(deq.popleft())
    else:
        deq.rotate(-1)
    count += 1


print("<%s>" %(', '.join(map(str,arr))))

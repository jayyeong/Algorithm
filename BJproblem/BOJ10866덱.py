from collections import deque
import sys

def main():
    deq = deque()

    N = int(input())

    for _ in range(N):
        S = sys.stdin.readline().split()
        #print(S)
        if S[0] == "push_front":
            deq.appendleft(S[1])
        elif S[0] == "push_back":
            deq.append(S[1])
        elif S[0] == "pop_front":
            if deq:
                print(deq.popleft())
            else:
                print(-1)
        elif S[0] == "pop_back":
            if deq:
                print(deq.pop())
            else:
                print(-1)
        elif S[0] == "size":
            print(len(deq))
        elif S[0] == "empty":
            if not deq:
                print(1)
            else:
                print(0)
        elif S[0] == "front":
            if deq:
                print(deq[0])
            else:
                print(-1)
        elif S[0] == "back":
            if deq:
                print(deq[-1])
            else:
                print(-1)

if __name__ == "__main__":
    main()
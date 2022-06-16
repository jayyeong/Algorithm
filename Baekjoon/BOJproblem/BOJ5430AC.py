from collections import deque

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = list(input())
    del p[-1]
    n = int(input())
    a = input().strip()
    if n != 0:
        de = deque(map(int,a[1:-1].split(sep=',')))
    else:
        de = deque()
    #print(p,aa)
    Reverseflag = False
    errorflag = False
    for s in p:
        if s == 'R':
            Reverseflag = not Reverseflag

        if s == 'D':
            if de:
                if Reverseflag:
                    de.pop()
                else:
                    de.popleft()

            else:
                errorflag = True
                break
    if errorflag:
        print("error")
    else:
        if Reverseflag:
            de.reverse()
        print("[%s]"%(','.join(map(str,de))))
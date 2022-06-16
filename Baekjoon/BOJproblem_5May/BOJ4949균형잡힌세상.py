from collections import deque
line = input()

while line != '.':
    deq = deque()

    for ch in line:
        if ch == '(':
            deq.append('(')
        elif ch == ')':
            if deq:
                if deq[-1] == '(':
                    deq.pop()
            else:
                deq.append('x')

        if ch == '[':
            deq.append('[')
        elif ch == ']':
            if deq:
                if deq[-1] == '[':
                    deq.pop()
            else:
                deq.append('x')

    if deq:
        print("no")
    else:
        print("yes")

    line = input()

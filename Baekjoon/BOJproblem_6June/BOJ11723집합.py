import sys
S = set()
for i in range(int(input())):
    command = sys.stdin.readline().rstrip()
    if command == 'all':
        S = set([x for x in range(1,21)])

    elif command == 'empty':
        S = set()

    else:
        c, num = command.split()
        n = int(num)
        if c == 'add':
            S.add(n)
        elif c == 'remove':
            S.discard(n)
        elif c == 'check':
            if n in S:
                print(1)
            else:
                print(0)
        else:
            if n in S:
                S.remove(n)
            else:
                S.add(n)
import sys
#input = sys.stdin.readline
N, M = map(int,input().split())
name_list = sys.stdin.read().splitlines()
no_hear = set(name_list[:N])
no_see = set(name_list[N:])
no_hear_see = list(no_see & no_hear)
no_hear_see.sort()

print(len(no_hear_see))
for s in no_hear_see:
    print(s)
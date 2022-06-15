import sys
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

no_hear = set()
no_see = set()

for _ in range(N):
    no_hear.add(input().rstrip())

for _ in range(M):
    no_see.add(input().rstrip())

no_hear_see = list(no_see & no_hear)
no_hear_see.sort()

print(len(no_hear_see))
for s in no_hear_see:
    print(s)
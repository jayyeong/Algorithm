E, S, M = map(int, input().split())
if E % 15 == 0:
    E = 0
if S % 28 == 0:
    S = 0
if M % 19 == 0:
    M = 0
for i in range(1,7981):
    if i % 15 == E and i % 28 == S and i % 19 == M:
        print(i)
        break
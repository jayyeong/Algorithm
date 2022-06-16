K = int(input())
s = []
for _ in range(K):
    N = int(input())
    if N == 0:
        s.pop()
    else:
        s.append(N)
print(sum(s))
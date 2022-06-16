N, K = map(int, input().split())
result = 0

while 1:
    a = (N//K) * K
    result += (N - a)
    N = a
    if N < K:
        break
    N //= K
    result += 1

result += (N - 1)
print(result)




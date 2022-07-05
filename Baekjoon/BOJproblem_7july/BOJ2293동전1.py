import sys
n, k = map(int,input().split())

coin = []
DP = [0 for _ in range(k + 1)]

for i in range(n):
    coin.append(int(sys.stdin.readline().rstrip()))
coin.sort()

DP[0] = 1 # 동전이 하나만 있을때 처리하기 위해 1로 설정

for c in coin:
    for i in range(c,k + 1):
        DP[i] += DP[i - c]
print(DP[k])
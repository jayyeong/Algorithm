N = int(input())
M = int(input())

if M != 0:
    broken_button = [int(x) for x in input().split()]
else:
    broken_button = []

result = abs(100 - N)

for num in range(1000001):
    n = [int(x) for x in list(str(num))]

    for i in range(len(n)):
        if n[i] in broken_button:
            break

        if i == len(n) - 1:
            count = len(n) + abs(N - num)
            result = min(result, count)
print(result)
# 최대한 가까이 채널이동
# 부족한 값은 +,- 버튼 눌러서 채우기
N = int(input())

a = N % 5
b = (N // 5) * 5
c = N - b
x = 0
if a % 3 == 0:
    x = a // 3 + N // 5 # 최적의 경우
else:
    if b > 0:
        while b > 0:
            b -= 5
            c += 5
            if b % 5 == 0 and c % 3 == 0:
                x = b//5+c//3
                break
            else:
                x = -1
    else:
        x = -1
print(x)
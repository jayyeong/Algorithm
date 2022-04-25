import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

# 1. 기존의 있는 나무들 사이 간견중 최소값 찾기
mlength = 1000000000
marr = []
for i in range(N - 1):
    marr.append(arr[i + 1] - arr[i])
    if arr[i + 1] - arr[i] < mlength:
        mlength = arr[i + 1] - arr[i]

a = []
result = 1000000000
for i in range(mlength,0,-1):
    step = 0
    for m in marr:
        if m % i != 0:
            step = 1000000000
            break
        step += m // i - 1
    if step <= result:
        result = step

print(result)
import math
n = int(input())
arr = [True] * (n + 1)
arr[0] = False
arr[1] = False

for i in range(2, int(math.sqrt(n)+1)):
    if arr[i] == True:
        j = 2

        while (i * j) <= n:
            arr[i*j] = False
            j += 1

left = 0
right = 0
temp_prime_sum = 0
count = 0
while left <= right:
    if temp_prime_sum > 0:
        left += 1
        temp_prime_sum
    else:

print(arr)
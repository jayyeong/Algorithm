N = int(input())
M = int(input())
S = input()

# P_n = 'I'
# for i in range(N):
#     P_n += 'OI'
# count = 0
#
# for i in range(len(S) - len(P_n)):
#     # print(S[i:i + len(P_n)])
#     if P_n == S[i:i + len(P_n)]:
#
#         count += 1

cursor, count, result = 0, 0, 0
while cursor < (M - 1):
    #print(S[cursor:cursor + 3])
    if S[cursor:cursor + 3] == 'IOI': #3칸짜리
        count += 1
        cursor += 2
        if count == N:
            result += 1
            count -= 1
    else:
        cursor += 1
        count = 0
print(result)
DP = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

for i in range(1,21):
    for j in range(1,21):
        for k in range(1,21):
            if i < j and j < k:
                DP[i][j][k] = DP[i][j][k - 1] + DP[i][j - 1][k - 1] - DP[i][j -1][k]
            else:
                DP[i][j][k] = DP[i - 1][j][k] + DP[i - 1][j - 1][k] + DP[i - 1][j][k - 1] - DP[i - 1][j - 1][k - 1]

while True:
    a, b, c = map(int,input().split())

    if a == -1 and b == -1 and c == -1:
        break

    elif a <= 0 or b <= 0 or c <= 0:
        result = DP[0][0][0]

    elif a > 20 or b > 20 or c > 20:
        result = DP[20][20][20]

    else:
        result = DP[a][b][c]

    print("w(",a,", ",b,", ",c,") = ",result,sep='')

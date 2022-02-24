while True:
    a, b, c = map(int,input().split())
    result = 0

    if a == -1 and b == -1 and c == -1:
        break

    if a <= 0 or b <= 0 or c <= 0:
        result = 1

    if a > 20 or b > 20 or c > 20:
        a, b, c = 20, 20, 20


    print("w(",a,", ",b,", ",c,") = ",result,sep='')

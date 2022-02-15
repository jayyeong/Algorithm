N, M, K = map(int,input().split())
box = [int(x) for x in input().split()]
box.sort(reverse=True)
a = box[0]
b = box[1]

print(a*(M%(K+1)) + (a*K + b)*(M // (K+1) ))


N = int(input())
box = []

for _ in range(N):
    box.append(input())
sbox = set(box)
a = list(sbox)

a.sort(key = lambda x:(len(x),x))

for x in a:
    print(x)
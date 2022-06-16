N = int(input())
first = ['***','* *','***']

def star(n,Arr: list):
    box = []
    if n == 3:
        return Arr
    else:
        for i in Arr:
            box.append(i*3)
        for i in Arr:
            box.append(i+' '*len(Arr)+i)
        for i in Arr:
            box.append(i*3)
        return star(n//3,box)

for s in star(N,first):
    print(s)
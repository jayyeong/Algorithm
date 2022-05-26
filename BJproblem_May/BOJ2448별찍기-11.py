N = int(input())
first = ['  *  ',' * * ','*****']
def star(n,Arr: list,count):
    box = []
    if n == 3:
        return Arr
    else:
        for i in Arr:
            box.append(' '*(3*(2**count))+i+' '*(3*(2**count)))
        for i in Arr:
            box.append(i+' '+i)

        return star(n//2,box,count + 1)

for s in star(N,first,0):
    print(s)

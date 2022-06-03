import sys
input = sys.stdin.readline

def find_root(x):
    if parent[x] != x:
        parent[x] = find_root(parent[x])
    return parent[x]

def union_root(x,y):
    a = find_root(x)
    b = find_root(y)
    if a != b:
        parent[b] = a

V, E = map(int,input().split())
box = []
parent = [i for i in range(V + 1)]
result = 0

for _ in range(E):
    a,b,c = map(int,input().split())
    box.append([a,b,c])

box.sort(key= lambda x : x[2])

for i in range(len(box)):
    v1 = box[i][0]
    v2 = box[i][1]
    if find_root(v1) != find_root(v2):
        union_root(v1,v2)
        result += box[i][2]

#print(parent)
print(result)
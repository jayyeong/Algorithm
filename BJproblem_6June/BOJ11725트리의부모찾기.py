import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

arr = [[] for i in range(N + 1)]
box = [0] * (N + 1)
visited = [False] * (N + 1)

for _ in range(N - 1):
    x,y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)
# print(arr)

def dfs(n):
    visited[n] = True
    #print(n)
    for i in arr[n]:
        if not visited[i]:
            box[i] = n
            dfs(i)
dfs(1)
#print(box)
for i in range(2,len(box)):
    print(box[i])

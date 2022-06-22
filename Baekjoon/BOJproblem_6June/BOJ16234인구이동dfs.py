import sys
sys.setrecursionlimit(10**4)
N, L, R = map(int,input().split())
country = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(N):
    country.append([int(x) for x in sys.stdin.readline().rstrip().split()])
visited = [[False]*N for _ in range(N)]

def dfs(x,y):
    global union_person
    visited[x][y] = True
    union_list.append([x,y])
    union_person += country[x][y]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if L <= abs(country[x][y] - country[nx][ny]) <= R:
                dfs(nx,ny)

population_flag = True
result = 0

while population_flag:
    population_flag = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union_list = []
                union_person = 0
                dfs(i,j)
                union_len = len(union_list)

                if union_len >= 2:
                    population_flag = True

                for u in union_list:
                    country[u[0]][u[1]] = union_person//union_len

    if population_flag:
        result += 1

print(result)
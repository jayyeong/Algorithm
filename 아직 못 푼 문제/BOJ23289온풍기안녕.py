import sys
R, C, K = map(int, input().split())

graph = []
checking_area = []
heater = []

for i in range(R):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(C):
        if 0 < graph[i][j] < 5:
            heater.append([graph[i][j], i, j])
            graph[i][j] = 0

        elif graph[i][j] == 5:
            checking_area.append([i, j])
            graph[i][j] = 0


W = int(input())

wall_list = []

for _ in range(W):
    wall_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

def wind():
    pass

def adjust():
    pass

def reduction():
    pass

def condition_check():
    for a in checking_area:
        x, y = a
        if graph[x][y] < K:
            return True
    return False

ans = 0

while True:

    wind()
    adjust()
    reduction()

    ans += 1

    if condition_check() == False:
        break

print(ans)
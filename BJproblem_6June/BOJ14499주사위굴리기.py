import sys
input = sys.stdin.readline
N, M, X, Y, K = map(int,input().rstrip().split())

dx = [0,0,-1,1]
dy = [1,-1,0,0] # 1 동, 2 서, 3 북, 4 남
dice = [0,0,0,0,0,0] # down left front back right up
road = []

for i in range(N):
    road.append([int(x) for x in input().rstrip().split()])
command = [int(x) for x in input().rstrip().split()]

#print(road)

def move_right():
    temp = dice[1]
    dice[1] = dice[0]
    dice[0] = dice[4]
    dice[4] = dice[5]
    dice[5] = temp

def move_left():
    temp = dice[4]
    dice[4] = dice[0]
    dice[0] = dice[1]
    dice[1] = dice[5]
    dice[5] = temp

def move_front():
    temp = dice[3]
    dice[3] = dice[0]
    dice[0] = dice[2]
    dice[2] = dice[5]
    dice[5] = temp

def move_back():
    temp = dice[5]
    dice[5] = dice[2]
    dice[2] = dice[0]
    dice[0] = dice[3]
    dice[3] = temp

x, y = X, Y
for i in command:
    if 0 <= x + dx[i - 1] < N and 0 <= y + dy[i - 1] < M:
        x, y = x + dx[i - 1], y + dy[i - 1]
        if i == 1:
            move_right()
        elif i == 2:
            move_left()
        elif i == 3:
            move_back()
        elif i == 4:
            move_front()

        if road[x][y] == 0:
            road[x][y] = dice[0]
        else:
            dice[0] = road[x][y]
            road[x][y] = 0
        print(dice[5])
import sys
N = int(input())
room = []
shark = []
for i in range(N):
    room.append([int(x) for x in sys.stdin.readline().rstrip().split()])
    for j in range(len(room[i])):
        if room[i][j] == 9:
            shark = [i,j]


print(room,shark)


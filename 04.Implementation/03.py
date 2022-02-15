pos = list(input())
moves = [[2,1],[2,-1],[1,2],[1,-2],[-1,2],[-1,-2],[-2,1],[-2,-1]]

x = ord(pos[0]) - 96
y = int(pos[1])
count = 0
for move in moves:
    if 1 <= x + move[0] <= 8:
        if 1 <= y + move[1] <= 8:
            count += 1
print(count)
        
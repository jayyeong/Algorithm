sudoku = []
for i in range(9):
    sudoku.append([int(x) for x in input().split()])
blankbox = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blankbox.append([i,j])

def row_check(row,in_num):
    for i in range(9):
        if in_num == sudoku[row][i]:
            return False
    return True

def col_check(col,in_num):
    for i in range(9):
        if in_num == sudoku[i][col]:
            return False
    return True

def rec_check(row,col,in_num):
    i, j = 0, 0
    if 0 <= row < 3:
        i = 0
    elif 3 <= row < 6:
        i = 3
    elif 6 <= row < 9:
        i = 6

    if 0 <= col < 3:
        j = 0
    elif 3 <= col < 6:
        j = 3
    elif 6 <= col < 9:
        j = 6

    for a in range(i, i + 3):
        for b in range(j, j + 3):
            if sudoku[a][b] == in_num:
                return False
    return True

def dfs(n):
    #print(n)
    if n == len(blankbox):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j],end=' ')
            print()
        exit(0)


    for a in range(1,10):
        x = blankbox[n][0]
        y = blankbox[n][1]
        if row_check(x,a) and col_check(y,a) and rec_check(x,y,a):
            #print(a)
            sudoku[x][y] = a
            dfs(n + 1)
            sudoku[x][y] = 0

dfs(0)
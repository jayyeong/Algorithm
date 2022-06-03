K = int(input())

side = []
length = []
edge = [[] for _ in range(5)]

for _ in range(6):
    x, y = map(int,input().split())
    side.append(x)
    length.append(y)
    edge[x].append(y)

if len(edge[2]) == 1 and len(edge[4]) == 1: # r
    Widx = side.index(4)
    Hidx = side.index(2)
    W = length[Widx]
    H = length[Hidx]
    sW = abs(length[(Widx - 1) % 6] - length[(Widx + 1) % 6])
    sH = abs(length[(Hidx - 1) % 6] - length[(Hidx + 1) % 6])
    print((W*H - sW*sH)*K)
if len(edge[2]) == 1 and len(edge[3]) == 1: # ㄴ
    Widx = side.index(2)
    Hidx = side.index(3)
    W = length[Widx]
    H = length[Hidx]
    sW = abs(length[(Widx - 1) % 6] - length[(Widx + 1) % 6])
    sH = abs(length[(Hidx - 1) % 6] - length[(Hidx + 1) % 6])
    print((W*H - sW*sH)*K)
if len(edge[3]) == 1 and len(edge[1]) == 1: # ㅢ
    Widx = side.index(3)
    Hidx = side.index(1)
    W = length[Widx]
    H = length[Hidx]
    sW = abs(length[(Widx - 1) % 6] - length[(Widx + 1) % 6])
    sH = abs(length[(Hidx - 1) % 6] - length[(Hidx + 1) % 6])
    print((W*H - sW*sH)*K)
if len(edge[1]) == 1 and len(edge[4]) == 1: # ㄱ
    Widx = side.index(1)
    Hidx = side.index(4)
    W = length[Widx]
    H = length[Hidx]
    sW = abs(length[(Widx - 1) % 6] - length[(Widx + 1) % 6])
    sH = abs(length[(Hidx - 1) % 6] - length[(Hidx + 1) % 6])
    print((W*H - sW*sH)*K)


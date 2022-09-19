import sys
from collections import deque
N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

road_map = []

for _ in range(N):
    road_map.append([int(x) for x in sys.stdin.readline().split()])

cur_value = 0
count = 0
def bfs():
    global count
    que = deque()
    que.append([0, 0, road_map[0][0]])

    while que:
        x, y, value = que.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if road_map[nx][ny] < value:
                    if nx == N - 1 and ny == M - 1:
                        count += 1
                    que.append([nx, ny, road_map[nx][ny]])
                    
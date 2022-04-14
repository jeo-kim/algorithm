import sys

n = int(input())
area = []
for _ in range(n):
    row = map(int, sys.stdin.readline().split())
    area.append(list(row))

max_h = 0
for row in area:
    if max(row) > max_h:
        max_h = max(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y):
    global rain
    if area[x][y] <= rain:
        return
    else:
        visited[x][y] = 1
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and area[new_x][new_y] > rain and visited[new_x][new_y] == 0:
                DFS(new_x, new_y)

max_ans = 0
for rain in range(max_h):
    visited = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > rain and visited[i][j] == 0:
                DFS(i,j)
                count += 1
    if count > max_ans:
        max_ans = count
print(max_ans)
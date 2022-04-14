import collections
import sys

m, n, h = map(int, input().split())

tomatoes = []

que = collections.deque()
dx = [0, 0, 0, 1, 0, -1]
dy = [0, 0, -1, 0, 1, 0]
dz = [-1, 1, 0, 0, 0, 0]

zero_exist = False
for k in range(h):
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    tomatoes.append(board)
    for i in range(n):
        for j in range(m):
            if tomatoes[k][i][j] == 1:
                que.append((k, i, j, 0))
            if tomatoes[k][i][j] == 0:
                zero_exist = True

if not zero_exist:  # 처음부터 다 익어있었다면
    print(0)

else:
    while que:
        tmp = que.popleft()

        for i in range(6):
            new_z = tmp[0] + dz[i]
            new_x = tmp[1] + dx[i]
            new_y = tmp[2] + dy[i]
            day = tmp[3] + 1
            if 0<=new_z<h and 0<=new_x<n and 0<=new_y<m and tomatoes[new_z][new_x][new_y] == 0:
                tomatoes[new_z][new_x][new_y] = 1
                que.append((new_z, new_x, new_y, day))

    completed = True
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomatoes[k][i][j] == 0:
                    completed = False
                    # print("완성 안 됨",-1)

    if not completed:
        print(-1)

    if completed:
        print(day-1)



board = [
    [1,0,1,0,0,1,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,1,0,1,0,1],
    [1,0,1,0,0,1,0,1,1,1],
    [1,0,1,0,0,1,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,0,1,0,0,1,0,1,1,1],
    [1,1,1,0,0,1,0,1,0,1],
    [1,0,1,0,0,1,1,1,0,1],
    [1,0,1,0,0,2,0,1,0,1]
]

visit = [[0]*10 for _ in range(10)]
dx = [0, 0, -1]
dy = [-1, 1, 0]
which_column = 0

def DFS(L, x, y):
    global which_column
    if x == 0:
        which_column = y
        return
    else:
        side_exist = False
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<10 and 0<=ny<10 and board[nx][ny]==1 and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                side_exist = True
                DFS(L+1, nx, ny)
        if side_exist is False:
            nx = x + dx[2]
            ny = y + dy[2]
            visit[nx][ny] = 1
            DFS(L+1, nx, ny)

for i in range(10):
    if board[9][i] == 2:
        DFS(0,9,i)

print(which_column)

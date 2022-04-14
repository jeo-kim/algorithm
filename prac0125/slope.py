m, n= map(int, input().split())

heights = []
for _ in range(m):
	heights.append(list(map(int, input().split())))

visited = [[0] * n for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0
def DFS(L:int, x, y):
    global count
    if (x, y) == (m-1, n-1):
        count += 1
        return
    else:
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x < m and 0 <= n_y < n:
                prev_h = heights[x][y]
                next_h = heights[n_x][n_y]
                if visited[n_x][n_y] == 0 and next_h < prev_h:
                    visited[n_x][n_y] = 1
                    DFS(L+1, n_x, n_y)
                    visited[n_x][n_y] = 0

DFS(0, 0, 0)
print(count)
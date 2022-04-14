import sys
sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)

visited = [[0]*m for _ in range(n)]
visited[0][0] = 1

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

count = 0
def DFS(i, j):
    global count
    if i == n-1 and j == m-1:
        count += 1
        return
    else:
        for k in range(4):
            adj_i = i + di[k]
            adj_j = j + dj[k]
            if 0<=adj_i<n and 0<=adj_j<m and graph[i][j] > graph[adj_i][adj_j] and visited[adj_i][adj_j] == 0:
                DFS(adj_i, adj_j)

DFS(0,0)
print(count)








# for i in range(n):
#     for j in range(m):
#         if i == 0 and j == 0:
#             dy[i][j] = 1
#         else:
#             for k in range(4):
#                 adj_i = i + di[k]
#                 adj_j = j + dj[k]
#                 if 0<=adj_i<n and 0<=adj_j<m and graph[i][j] < graph[adj_i][adj_j]:
#                     dy[i][j] += dy[adj_i][adj_j]
#
# for row in dy:
#     print(row)
#
#
# print(dy[n-1][m-1])

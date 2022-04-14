import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)

dy = [[0]*m for _ in range(n)]
dy[0][0] = 1

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        # if i == 0 and j == 0:
        #     dy[i][j] = 1
        # else:
        for k in range(4):
            adj_i = i + di[k]
            adj_j = j + dj[k]
            if 0<=adj_i<n and 0<=adj_j<m and graph[i][j] > graph[adj_i][adj_j]:
                dy[adj_i][adj_j] += dy[i][j]
                # dy[adj_i][adj_j] += 1

        # print(f"{i}, {j} 갱신하고 {dy[i]}")

#
# x = 0
# y = 0

# while True:
#     if x == n-1 and y == m-1:
#         break
#
#


for row in dy:
    print(row)


print(dy[n-1][m-1])

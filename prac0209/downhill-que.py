import collections
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)

que = collections.deque()
que.append((0,0))

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

count = 0

while que:
    row, col = que.popleft()

    if row == n-1 and col == m-1:
        count += 1
        continue

    for k in range(4):
        adj_i = row + di[k]
        adj_j = col + dj[k]
        if 0 <= adj_i < n and 0 <= adj_j < m and graph[row][col] > graph[adj_i][adj_j]:
            que.append((adj_i, adj_j))

print(count)
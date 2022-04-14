import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

INF = int(1e18)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i, row in enumerate(graph):
    row[i] = 0

for i in range(m):
    s, d, c = map(int, sys.stdin.readline().split())
    graph[s][d] = min(graph[s][d], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, len(graph)):
    for j in range(1, len(graph[0])):
        if graph[i][j] == INF:
            graph[i][j] = 0

for row in graph[1:]:
    line = " ".join(list(map(str, row[1:])))
    print(line)
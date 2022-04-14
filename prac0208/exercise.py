import sys

V, E = map(int, sys.stdin.readline().split())
INF = int(1e8)

graph = [[INF] * (V+1) for _ in range(V+1)]

# 최단거리를 갱신해갈 2차원 배열
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u][v] = w

# 경유지 고려하며 최단거리 갱신하기
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = INF
# 자신에게로 향하는 거리들 구해보고 그 중 최소인 것으로 answer 갱신
for i in range(1, len(graph)):
    if graph[i][i] == INF:
        continue
    answer = min(answer, graph[i][i])

# 정답 제출 / 자신에게로 오는 게 모두 불가능했다면 -1리턴
if answer == INF:
    print(-1)
else:
    print(answer)

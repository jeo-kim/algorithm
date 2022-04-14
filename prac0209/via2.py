import heapq
import sys

N, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append((e, c))
    graph[e].append((s, c))

v1, v2 = map(int, sys.stdin.readline().split())

que = []
heapq.heappush(que, (0, 1, [1]))
exist = False

while que:
    cost, now, visited = heapq.heappop(que)
    if now == N and v1 in visited and v2 in visited:
        print(cost)
        exist = True
        break
    else:
        for nxt, d_c in graph[now]:
            new_cost = cost + d_c
            new_visit = visited + [nxt]
            heapq.heappush(que, (new_cost, nxt, new_visit))

if not exist:
    print(-1)

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
heapq.heappush(que, (0, v1))

v1_to_v2 = 0

while que:
    cost, node = heapq.heappop(que)

    if node == v2:
        v1_to_v2 = cost
        que.clear()
        break
    for nxt, d_c in graph[node]:
        new_cost = cost + d_c
        heapq.heappush(que, (new_cost, nxt))

heapq.heappush(que, (0, 1))
start_to_v1 = 0
while que:
    cost, node = heapq.heappop(que)

    if node == v1:
        start_to_v1 = cost
        que.clear()
        break
    for nxt, d_c in graph[node]:
        new_cost = cost + d_c
        heapq.heappush(que, (new_cost, nxt))

heapq.heappush(que, (0, 1))
start_to_v2 = 0
while que:
    cost, node = heapq.heappop(que)

    if node == v2:
        start_to_v2 = cost
        que.clear()
        break
    for nxt, d_c in graph[node]:
        new_cost = cost + d_c
        heapq.heappush(que, (new_cost, nxt))

heapq.heappush(que, (0, N))
n_to_v1 = 0
while que:
    cost, node = heapq.heappop(que)

    if node == v1:
        n_to_v1 = cost
        que.clear()
        break
    for nxt, d_c in graph[node]:
        new_cost = cost + d_c
        heapq.heappush(que, (new_cost, nxt))

heapq.heappush(que, (0, N))
n_to_v2 = 0
while que:
    cost, node = heapq.heappop(que)

    if node == v2:
        n_to_v2 = cost
        que.clear()
        break
    for nxt, d_c in graph[node]:
        new_cost = cost + d_c
        heapq.heappush(que, (new_cost, nxt))

candidate1= start_to_v1 + v1_to_v2 + n_to_v2
candidate2 = start_to_v2 + v1_to_v2 + n_to_v1
print(candidate1, candidate2)

print(min(candidate1, candidate2))



#
# for row in graph:
#     print(row)
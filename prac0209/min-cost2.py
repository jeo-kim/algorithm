import heapq
import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

buses = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    buses[s].append((e, c))

start, dst = map(int, sys.stdin.readline().split())

# 최소 비용부터 뽑아낼 큐
que = [(0, start, [start])]

answers = []

while que:
    cost, now, visited = heapq.heappop(que)
    if now == dst:
        answers.append(cost)
        answers.append(len(visited))
        answers.append(visited)

        break
    else:
        for nxt, d_c in buses[now]:
            new_cost = cost + d_c
            new_visit = visited + [nxt]
            heapq.heappush(que, (new_cost, nxt, new_visit))

for i, answer in enumerate(answers):
    if i != 2:
        print(answer)
    else:
        print(" ".join(map(str, answer)))

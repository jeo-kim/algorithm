import heapq
import sys

n, m = map(int, sys.stdin.readline().split())

con_info = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    con_info[s].append(e)
    con_info[e].append(s)

# 출발점에서 각 노드(헛간)에 이르는 최단거리 테이블 준비 (INF 로 초기화)
INF = int(1e9)
min_dis = [INF] * (n+1)
min_dis[1] = 0

# 해당 시점마다 출발지로부터 가장 가까운 노드들을 가져와서, 그 노드를 경유하는 루트를 고려할 것
# 가까운 것부터 가져오기 위해 최소힙 사용
que = []
heapq.heappush(que, (0, 1))

while que:
    dis, node = heapq.heappop(que)
    # 이미 해당 노드에 대해 (방문해서) 처리한 적이 있어서,
    # 지금 꺼내 본 경로의 거리보다 더 짧은 거리로 min_dis 테이블이 업데이트 되어 있다면 지금 꺼낸 친구는 무시하도록
    if min_dis[node] < dis:
        continue
    # 해당 노드로 가는 가장 짧은 거리로 인정받는다면, 이 노드를 경유하여 갈 수 있는 다른 인접노드(i)에 대해
    # 경유할 경우의 비용을 계산해본다 (cost)
    # 기존에 그 인접노드들에 가려면 필요했던 거리인 min_dis[i] 보다 새로 산정한 비용(cost)이 적다면
    # 최소 거리를 갱신(min_dis) , 그리고 그 i 노드까지 cost 의 비용으로 지나는 경로를 고려해볼 수 있으므로
    # que 에 다시 넣어줌.
    else:
        for i in con_info[node]:
            cost = dis + 1
            if cost < min_dis[i]:
                min_dis[i] = cost
                heapq.heappush(que, (cost, i))

# 출력할 아이들(제일 먼 헛간까지의 거리, 그런 거리를 갖는 헛간의 수, 그런 헛간들 중에 인덱스가 가장 작은 것)
max_dis = max(min_dis[1:])
cnt = min_dis.count(max_dis)
min_idx = min_dis.index(max_dis)

print(min_idx, max_dis, cnt)


import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
s = int(sys.stdin.readline().rstrip())

# 연결 정보 받아오는 중첩리스트
conn_info = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    conn_info[u].append((v, w))

# 초기화에 사용/도달불가한 노드 알아볼 큰 수
INF = int(1e12)

# 최단거리 테이블
min_dis = [INF] * (n+1)
min_dis[s] = 0

# 시작점 미리 넣기 (거리, 해당노드) 튜플로
que = [(0, s)]

while que:
    w, it = heapq.heappop(que)
    # 이 노드로 오는 경로로 기존에 기록된 것이 더 효율적이라면, 이 경로 무시
    if min_dis[it] < w:
        continue
    # 이 노드에서 다른 인접 노드로 가는 경로에 대한 비용 고려해보고 그 인접노드로 가는 기존 비용보다 적다면 갱신.
    # 괜찮은 경로이므로 다음 경유할 때 고려할 수 있을 경로이니 우선순위큐(heapq) 에 넣기
    for to_node, d_w in conn_info[it]:
        cost = w + d_w
        if cost < min_dis[to_node]:
            min_dis[to_node] = cost
            heapq.heappush(que, (cost, to_node))

for i in range(1, n+1):
    if min_dis[i] >= INF:
        print("INF")
    else:
        print(min_dis[i])

# print(min_dis)

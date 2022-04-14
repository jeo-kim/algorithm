import heapq
import sys

# n X n 의 탐사 지형(?) 정보 받아와서 2차원 배열로 그리기
n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n)]
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph[i] = row

# 초기화에 사용할 큰 수
INF = int(1e9)

# 아직 접근 가능한 좌표와 경로 전혀 취하지 않았으니까 모든 좌표는 큰 수로 초기화, 시작점은 자신의 칸에서의 소모량으로 초기화
consumption = [[INF] * n for _ in range(n)]
consumption[0][0] = graph[0][0]

# 상 우 하 좌 이동을 위한 행과 열의 차이값들 준비
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 최소 에너지소모량을 위해 해당 지점에서의 에너지소모량을 기준으로 삼도록할 최소힙을 위한 리스트 준비
# 시작점 넣기(에너지량, 좌표튜플)
que = []
heapq.heappush(que, (consumption[0][0], (0, 0)))

# 매번 최소 에너지 소모량인 지점을 꺼냄
while que:
    energy, loc = heapq.heappop(que)
    x, y = loc[0], loc[1]

    # 지금 꺼낸 에너지보다 기존에 해당 좌표에 기록해놓은 에너지소모량이 적다면
    # 이미 앞서서 꺼냈던 경로에 의해 x,y에 대한 더 효율적인(에너지소모량이 적은) 방법이 발견되었으므로
    # 지금 꺼낸 아이는 무시.
    if consumption[x][y] < energy:
        continue
    # 기존 정보보다 에너지소모가 더 크지 않다면 괜찮을 수 있는 경로이므로
    else:
        for k in range(4):
            adj_x = x + dx[k]
            adj_y = y + dy[k]
            # 여기서 이동 가능한 네 방향으로 뻗어보고, 유효한 인덱스 범위 내에 있다면
            # 지금 지점까지 오는 데 소모하는 에너지 + 다음 칸으로 가는 데 드는 에너지를 합하여 새로운 에너지 소모량 구하고
            # 그게 기존에 기록된 에너지소모량보다 적다면 더 좋은 경로 발견한 것이므로 갱신하고
            # 해당 경로를 바탕으로 더 조사할 수 있으므로 heapq 에 넣어준다.
            if 0 <= adj_x < n and 0 <= adj_y < n:
                cost = energy + graph[adj_x][adj_y]
                if cost < consumption[adj_x][adj_y]:
                    consumption[adj_x][adj_y] = cost
                    heapq.heappush(que, (cost, (adj_x, adj_y)))

# 최소 에너지소모를 선택해가며 목표지점에 도달했을 때의 값 출력
print(consumption[n - 1][n - 1])
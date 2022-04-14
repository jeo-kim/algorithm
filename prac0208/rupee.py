import heapq
import sys

cnt = 0
while True:
    cnt += 1
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    graph = [[] for _ in range(n)]
    for i in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        graph[i] = row

    # 각 칸에 이를 때의 손실액 최소로 기록해갈 배열, 그리고 초기화에 사용할 큰 수
    INF = int(1e9)
    lost = [[INF] * n for _ in range(n)]
    # 출발점에서의 손실액은 미리 정해둘 수 있음
    lost[0][0] = graph[0][0]

    # 상 우 하 좌 이동할 때 필요
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 손실액 적은 경로(?)부터 뽑아낼 우선순위큐(heap), 출발점 넣어둠
    que = [(lost[0][0], 0, 0)]  # 손실액, 행, 열
    while que:
        cost, i, j = heapq.heappop(que)
        if lost[i][j] < cost:
            continue
        for k in range(4):
            new_i = i + dx[k]
            new_j = j + dy[k]
            if 0<=new_i<n and 0<=new_j<n:
                new_cost = cost + graph[new_i][new_j]
                if new_cost < lost[new_i][new_j]:
                    lost[new_i][new_j] = new_cost
                    heapq.heappush(que, (new_cost, new_i, new_j))

    print(f"Problem {cnt}: {lost[n-1][n-1]}")





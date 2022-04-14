import heapq

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4]]

def solution(n, edge):
    # 매우 큰 수(초기화에 사용)
    INF = int(1e9)

    # 시작 노드 번호(이 문제에서 1번노드)
    start = 1

    # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
    graph = [[] for i in range(n+1)]

    # 최단거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (n+1)

    # 모든 간선 정보를 적용하기
    for i in range(len(edge)):
        n1, n2 = edge[i][0], edge[i][1]
        graph[n1].append(n2)
        graph[n2].append(n1)


    def dijkstra(start):
        q = []
        # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
        heapq.heappush(q, (0, start))

        # 시작 노드에 대해서 초기화
        distance[start] = 0

        while q:
            # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            dist, now = heapq.heappop(q)
            # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            # ==> 앞서 먼저 처리되었다면, 더 짧은 경로가 반영되었다는 뜻이니까!
            # (큐에서 먼저나온 아이가 처리한 거면, 더 작은 거리가 반영된 것)
            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 다른 노드를 확인
            for i in graph[now]:
                cost = distance[now] + 1
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))

    dijkstra(start)

    # 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(1, n+1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if distance[i] == INF:
            print(f"{start}에서 {i}노드에는 도달 불가합니다.")
        else:
            print(f"{start}에서 {i}노드까지의 거리는 {distance[i]}입니다.")


    # 가장 먼 노드의 개수를 리턴하기 위한 곳
    max_dis = max(distance[1:])
    answer = distance.count(max_dis)

    return answer


#     # 모든 노드로 가기 위한 최단 거리를 출력
#     for i in range(1, n+1):
#         # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
#         if distance[i] == INF:
#             print(f"{start}에서 {i}노드에는 도달 불가합니다.")
#         else:
#             print(f"{start}에서 {i}노드까지의 거리는 {distance[i]}입니다.")
#
#
solution(n, edge)
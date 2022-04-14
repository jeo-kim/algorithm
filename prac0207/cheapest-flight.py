import collections
import heapq
import time

start = time.time()

# def findCheapestPrice(n, flights, src, dst, K):
#     graph = collections.defaultdict(dict)
#     for s, d, w in flights:
#         graph[s][d] = w
#     pq = [(0, src, K+1)]
#     vis = [0] * n
#     while pq:
#         w, x, k = heapq.heappop(pq)
#         if x == dst:
#             return w
#         if vis[x] >= k:
#             continue
#         vis[x] = k
#         for y, dw in graph[x].items():
#             heapq.heappush(pq, (w+dw, y, k-1))
#     return -1


def findCheapestPrice(n, flights, src, dst, K):
    # 공항 간 연결정보와 비용을 담아두는 곳
    # 출발지를 key 로, (도착지, 비용) 튜플들을 원소로하는 리스트를 value 로 하는 dictionary
    graph = collections.defaultdict(list)
    for s, d, c in flights:  # start, destination, cost
        graph[s].append((d, c))

    # 누적경로에 대한 정보를 하나씩 뽑아서 그 경로를 취해서 경유해갈 것인지 아닌지를 볼 것임
    # 이 때 저비용 우선으로 뽑히게끔 (비용, 현재노드, 앞으로 이동 가능한 횟수) 이렇게 튜플의 순서를 설정
    # 출발점에서의 누적경로 정보를 큐에 넣어둠.
    que = [(0, src, K+1)]

    # 지금까지 어떤 노드(공항)를 방문했는데, 거기까지 갔을 때 앞으로 더 이동 가능한 횟수가 얼마였는지를 기록할 일차원 배열.
    # 이것을 참고하면, 이미 앞서서 해당 공항을 방문한 누적경로가 당연히 저비용인데, 심지어 이후에 나온 누적경로보다, 앞으로 이동가능한 횟수가 같거나 많을 경우,
    # 이후에 나온 누적경로는 바로 무시할 수 있다는 점에서 가지치기에 유용하다. --> 시간 효율에 중요한 친구
    vis = [0] * n

    # 검토할 가치가 있는 누적경로를 담아놓고 최소 비용부터 뽑아볼 heapq.
    while que:
        c, x, m = heapq.heappop(que)
        if x == dst:
            return c
        # 이전에 이 노드를 방문했던 누적경로가 앞으로 이동가능한 횟수보다 지금 방문한 누적경로가 앞으로 이동가능한 횟수가 더 적다면
        # 지금 꺼낸 누적경로는 검토할 가치 없음.(이전에 등장했던 친구보다 비용도 더 드는데, 앞으로 이동가능한 횟수도 여유가 없으니까)
        if vis[x] >= m:
            continue
        # 앞으로 이동가능한 횟수가 기존에 등장했던 것보다는 여유가 있으니 dst 에 도달할 후보자격 얻음
        # 이후에 x를 경유하는 다른 누적경로가 등장할 시, 앞으로 이동가능한 횟수 비교해보기 위한 정보로 지금 이 경로의 m을 vis[x]에 업데이트
        vis[x] = m

        # x 를 경유해서 x 와 인접한 곳으로 가는 누적 경로를 heapq 에 push
        # 그리고 이때 x도 지나서 하나 더 간 것이므로 앞으로의 이동가능횟수를 나타내는 m도 -=1 해서 넣기
        for new, d_cost in graph[x]:
            heapq.heappush(que, (c+d_cost, new, m-1))
    return -1


# print(findCheapestPrice(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1), 6)
print(findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 0, 2, 2), 7)
print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1), 200)
print(findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0), 500)

print(time.time()-start)
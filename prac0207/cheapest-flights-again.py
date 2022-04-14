import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):

        # 항공편 연결/비용 정보 참고할 테이블
        con_info = [[] for _ in range(n)]
        for s, e, c in flights:  # start, end, cost
            con_info[s].append((e, c))

        # 비용 적은 루트부터 뽑아볼 que
        que = []
        # 비용, 현재노드, 경유횟수(출발점은 경유횟수 -1로 해야 직항인 곳의 경유 횟수를 0으로 할 수 있음) - 이렇게 묶어서 힙큐에 넣어줌.
        heapq.heappush(que, (0, src, -1))

        while que:
            cost, now, cnt = heapq.heappop(que)

            # 비용 적은 것부터 뽑고 있는 중인데, 목적지가 등장했다면, 목적지에 갈 수 있는 최소비용이니 정답으로 리턴
            if now == dst:
                return cost
            # 방금 뽑아낸 경로가 경유했던 횟수(cnt)가 k보다 적을 때만 최소비용을 다시 고려하고 업데이트하는 과정을 실행.
            if cnt < k:
                # 지금 뽑아낸 노드와 인접한 것들을 con_info 에서 참고
                for nxt, c in con_info[now]:
                    # 현재 노드까지 오는데 들었던 비용(cost) + 현재 노드에서 다음 인접노드(nxt)로 가는 데 들 비용(c) = 새로 산정한 비용
                    new_cost = cost + c
                    heapq.heappush(que, (new_cost, nxt, cnt+1))


        # 위에서 경유 k 번만에 now 로서 dst 를 만나지 못했다면 return -1
        return -1

sol = Solution()
print(sol.findCheapestPrice(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1), 6)
print(sol.findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 0, 2, 2), 7)
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1), 200)
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0), 500)

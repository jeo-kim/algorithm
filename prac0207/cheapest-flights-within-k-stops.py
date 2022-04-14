import heapq


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):

        INF = int(1e9)

        costs = [INF] * (n)
        costs[src] = 0

        con_info = [[] for _ in range(n)]

        for flight in flights:
            s, e, c = flight[0], flight[1], flight[2]
            con_info[s].append((e, c))

        que = []
        # 비용, 현재 지점, 지금까지 경유 수
        heapq.heappush(que, (0, src, -1))
        cnt = 0
        while que:
            # if cnt > k:
            #     break

            c, now, stops = heapq.heappop(que)

            if costs[now] < c:
                continue
            else:
                for adj in con_info[now]:
                    adj_n, adj_c = adj[0], adj[1]
                    if adj_n == dst and stops == k:
                        break

                    cost = c + adj_c
                    if cost < costs[adj_n]:
                        # if adj_n == dst and stops == k:
                        #     break
                        costs[adj_n] = cost
                        heapq.heappush(que, (cost, adj_n, stops + 1))
            cnt += 1

        if costs[dst] >= INF:
            answer = -1
        else:
            answer = costs[dst]

        print(answer)
        return answer


sol = Solution()
# sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0)

# print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1), 200)
# print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0), 500)
print(sol.findCheapestPrice(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1), 6)

# 0
# 3
# 1

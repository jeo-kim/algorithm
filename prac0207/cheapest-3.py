import collections
import heapq

## 교재
class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int) -> int:

        graph = collections.defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        que = [(0, src, K)]

        while que:
            price, node, k = heapq.heappop(que)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(que, (alt, v, k-1))

        return -1

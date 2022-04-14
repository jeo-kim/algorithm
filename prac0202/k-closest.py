import heapq
import math

points = [[1,3],[-2,2]]
k = 1

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        distances = []
        result = []

        for i, point in enumerate(points):
            distance = math.sqrt(point[0]*point[0] + point[1]*point[1])
            # 거리를 우선순위 기준으로 하고, 거리와 해당 좌표가 points 에서 지녔던 index 도 함께 튜플에 넣기
            heapq.heappush(distances, (distance, i))


        for _ in range(k):
            idx = heapq.heappop(distances)[1]
            point = points[idx]
            result.append(point)

        return result


sol = Solution()
sol.kClosest(points, k)

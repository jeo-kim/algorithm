# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Input: nums = [1], k = 1
# Output: [1]

import collections
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        my_dict = collections.defaultdict(int)

        for num in nums:
            my_dict[num] += 1

        heap = []  # 최댓값을 항상 맨 앞에 놔줄 heap 준비
        for which_num, how_many in my_dict.items():

            # 파이썬의 heap 은 최소 heap 만 지원한다고 하므로,
            # how_many 의 부호를 바꿔준다. 그러면 가장 컸던 수부터 루트로 뽑아낼 수 있음.
            # 그리고 출력해야 하는 것은 which_num 이므로 우선순위를 결정하는 how_many 와 함께 which_num 을 패킹한다.
            heapq.heappush(heap, (-how_many, which_num))

        result = []
        for _ in range(k):
            # k 번만 최대를 뽑아내면 되고, 특히 패킹했던 것 중 후자(which_num)을 뽑아내면 된다.
            a, b = heapq.heappop(heap)
            result.append(b)

        return result

nums = [1,1,1,2,2,3]
k = 2

sol = Solution()
sol.topKFrequent(nums, k)
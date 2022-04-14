class Solution:
    def maxSubArray(self, nums) -> int:
        # 각 인덱스의 숫자를 끝점으로 하는 배열들 중 최대합을 적어가기 위한 기록 테이블
        n = len(nums)
        record = [0] * n
        record[0] = nums[0]

        for i in range(1, n):
            # 이전칸까지의 최대합이 음수면 이전의 정보는 반영 안하고 자신만을 반영
            if record[i-1] < 0:
                record[i] = nums[i]
            # 이전칸까지 최대합이 양수면 더하는 게 무조건 나으므로 반영하여 자신도 추가
            else:
                record[i] = record[i-1] + nums[i]

        return max(record)


nums1 = [5,4,-1,7,8]

sol = Solution()
sol.maxSubArray(nums1)
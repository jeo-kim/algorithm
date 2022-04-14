class Solution:
    def rob(self, nums) -> int:

        # nums 원소가 한 개일 경우 그냥 해당 원소 값을 리턴
        if len(nums) == 1:
            return nums[0]

        # 빈 0번 인덱스 추가된 상태로 nums 수정
        tmp = [0]
        new_nums = tmp + nums

        # 각 칸을 끝으로 턴다고 가정할 때, 훔칠 수 있는 최대를 기록하는 배열
        dy = [0] * len(new_nums)

        answer = 0
        # i는 fixed 할 인덱스 (1번과 2번)
        for i in range(1, 3):
            dy[i] = new_nums[i]
            for j in range(i+2, len(new_nums)):
                dy[j] = max(dy[j-2], dy[j-3]) + new_nums[j]
            candidate = max(dy)
            answer = max(answer, candidate)

        return answer

nums = [2,7,9,3,1]
sol = Solution()
sol.rob(nums)



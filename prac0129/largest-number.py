nums = [10,2]
# # #
# str_nums = list(map(str, nums))
# str_nums.sort(key=lambda x : x[0], reverse=True)
print(f"앞자리 큰 순으로 1차 정렬: {nums}")


class Solution(object):
    def largestNumber(self, nums):

        # 0만 들어왔을 경우에 대한 예외 처리
        # ([0,0] -> output: "0" 이어야 한다고 함)
        if max(nums) == 0:
            return "0"

        # 일단 맨 앞자리 숫자가 큰것들을 앞쪽으로 둔다.
        str_nums = list(map(str, nums))
        # str_nums.sort(key=lambda x: x[0], reverse=True)

        # 이제 삽입 정렬을 사용해서, 인접한 두 수를 바꾸어 조합했을 때 더 큰 수가 나오도록
        # 필요하다면 스왑해간다.
        for cur in range(1, len(str_nums)):
            # 두번째 수부터 비교 시작
            for delta in range(1, cur + 1):
                # 비교대상이 될 친구는 자기보다 바로 앞(delta = 1)일때부터 맨 첫 번째아이([0])까지 가야 하니까
                # (물론 그렇게 앞으로 비교대상이 진행한다면, 비교가 될 나도 계속 스왑으로 인해 하나씩 앞으로 가는 것이고)
                # 그러면 원래 나의 값은 [cmp +1]의 인덱스로 가리켜 볼 수 있음.
                cmp = cur - delta
                # <앞선 친구 - 나>를 조합해서 만든 수의 크기와, <나-앞서있던친구> 조합으로 만든 수의 크기를 비교해봄!
                # 만약 순서를 바꿔야 더 크다면, 바꾸기!
                if int(str_nums[cmp] + str_nums[cmp + 1]) < int(str_nums[cmp + 1] + str_nums[cmp]):
                    str_nums[cmp], str_nums[cmp + 1] = str_nums[cmp + 1], str_nums[cmp]
                else:
                    break

        # 하나의 문자열로 제출
        answer = "".join(map(str, str_nums))
        return answer

sol = Solution()
print(sol.largestNumber(nums))
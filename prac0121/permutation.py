import collections
class Solution(object):
    def permute(self, nums:list):
        # tip for me : 중복이 없어야 한다, 이를 위해 "checked 여부 확인할 친구"를 만들어 두고 사용한다.
        # 인프런 강의에선 array 로 사용했고, 중복 확인할 숫자가 0-n 이렇게 순차저으로 주어져 있었어서 index 를 그 key 처럼 쓸 수 있었던 듯한데,
        # nums 가 0 또는 1부터 순차적으로 주어지지 않으면 어떻게 해야 하나 고민하다가
        # 나는 일단 딕셔너리로 해보면 어떨까 했다.

        res = [0] * len(nums)

        checked_dict = collections.defaultdict(int)
        for num in nums:
            checked_dict[num] = 0

        print("checked_dict: ", checked_dict)

        result_list = []

        def DFS(L):
            if L == len(nums):
                result = res[:]
                result_list.append(result)
                return
            else:
                for num in nums:
                    if checked_dict[num] == 0:  # 전 칸들에서 num 를 사용하지 않은 경우에만 num 쓸 수 있도록. (중복 방지)
                        checked_dict[num] = 1  # 이제 사용할 거니까 체크인.
                        res[L] = num  # 현재 레벨(인덱스(?))에 이 num 을 기입해주고
                        DFS(L+1)  # 한 레벨 더 들어가서 작동하도록 해준다. 지금 막 L 레벨에서 checked 한 것은 L + 1 이상의 깊이에서 쓸모 있음.
                        checked_dict[num] = 0  # 밖으로 나올 때는 다시 checked 여부를 돌려놓아야 한다!

        DFS(0)
        return result_list


nums1 = [1,2,3]
permute(nums1)
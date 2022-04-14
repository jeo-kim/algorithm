class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = ["@"]*len(nums)
        result_list = []

        def DFS(L):
            if L == len(nums):
                result = res[:]
                while -1 in result:
                    result.remove("@")
                result_list.append(result)
                return

            else:
                res[L] = nums[L]
                DFS(L+1)
                res[L] = "@"
                DFS(L+1)

        DFS(0)
        return result_list

sol = Solution()
nums1 = [1, 2, 3]
sol.subsets(nums1)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = [0] * k
        result_li = []

        def DFS(L, starter):
            if L == k:
                result = res[:]
                result_li.append(result)
                return

            if starter > n:
                return

            else:
                for i in range(starter, n+1):
                    res[L] = i
                    DFS(L+1, i+1)

        DFS(0, 1)

        return result_li

sol = Solution()
sol.combine(5, 2)
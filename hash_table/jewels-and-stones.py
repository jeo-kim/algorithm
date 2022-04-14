# class Solution(object):
#     def numJewelsInStones(self, jewels, stones):
#         """
#         :type jewels: str
#         :type stones: str
#         :rtype: int
#         """
#         jewel_dict = {}
#
#         for char in jewels:
#             jewel_dict[char] = 0
#
#         total_count = 0
#         for key, value in jewel_dict.items():
#             if key in stones:
#                 count = stones.count(key)
#                 # jewel_dict[key] += count  # ... 필요가 없다..?
#                 total_count += count
#
#         return total_count

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """

        total_count = 0
        for char in jewels:
            if char in stones:
                count = stones.count(char)
                total_count += count

        return total_count

        print(jewel_dict)
        print(total_count)


jewels = "aA"
stones = "aAAbbbb"

sol = Solution()
sol.numJewelsInStones(jewels, stones)
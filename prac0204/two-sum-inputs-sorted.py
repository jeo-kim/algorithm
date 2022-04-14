import bisect

numbers1 = [2,7,11,15]
target1 = 9

numbers2 = [2,3,4]
target2 = 6

numbers3 = [-1,0]
target3 = -1

# class Solution(object):
#     def twoSum(self, numbers, target):
#         """
#         :type numbers: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         res = []
#         def binary_search(arr, target, start, end):
#             if start > end:
#                 return None
#             mid = (start + end) // 2
#             if arr[mid] == target:
#                 return mid
#             else:
#                 if arr[mid] < target:
#                     return binary_search(arr, target, mid + 1, end)
#                 else:
#                     return binary_search(arr, target, start, mid - 1)
#
#         for i, num1 in enumerate(numbers):
#             now_target = target - num1
#             i2 = binary_search(numbers, now_target, i+1, len(numbers)-1)
#             if i2:
#                 res.append(i+1)
#                 res.append(i2+1)
#             else:
#                 continue
#
#         return res


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        for k, v in enumerate(numbers):
            left, right = k+1, len(numbers)-1
            expected = target - v
            while left <= right:
                mid = (left+right)//2
                if numbers[mid] == expected:
                    return k+1, mid+1
                elif numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1




sol = Solution()
# sol.twoSum(numbers1, target1)
# sol.twoSum(numbers2, target2)
sol.twoSum(numbers3, target3)
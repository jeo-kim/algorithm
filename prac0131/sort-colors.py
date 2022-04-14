nums1 = [2, 0, 2, 1, 1, 0]
nums2 = [2, 0, 1]

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        print(f"정렬 전: {nums}")

        def quick_sort(lt, rt):
            if lt < rt:
                pivot = nums[rt]
                i = lt
                for j in range(lt, rt):
                    if nums[j] <= pivot:
                        nums[j], nums[i] = nums[i], nums[j]
                        i += 1
                nums[rt], nums[i] = nums[i], nums[rt]
                quick_sort(lt, i-1)
                quick_sort(i+1, rt)

        quick_sort(0, len(nums)-1)

        print(f"정렬 후: {nums}")

sol = Solution()
sol.sortColors(nums1)
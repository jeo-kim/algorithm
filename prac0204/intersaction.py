nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = set()
        nums2.sort()

        def bs(arr, t, s, e):
            if s > e:
                return None

            mid = (s+e)//2
            if arr[mid] == t:
                return mid
            elif arr[mid] < t:
                return bs(arr, t, mid+1, e)
            elif arr[mid] > t:
                return bs(arr, t, s, mid-1)


        for target in nums1:
            idx = bs(nums2, target, 0, len(nums2)-1)
            if idx is None:
                continue
            else:
                res.add(nums2[idx])

        return list(res)


sol = Solution()
sol.intersection(nums1, nums2)
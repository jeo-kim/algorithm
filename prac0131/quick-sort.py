nums1 = [1, 4, 3, 5, 2, 9]

def quick_sort(nums, lt, rt):
    if lt < rt:
        pivot = nums[rt]
        pos = lt
        for i in range(lt, rt):
            if nums[i] <= pivot:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
        nums[pos], nums[rt] = nums[rt], nums[pos]
        quick_sort(nums, lt, pos-1)
        quick_sort(nums, pos+1, rt)

quick_sort(nums1, 0, 5)
print(nums1)

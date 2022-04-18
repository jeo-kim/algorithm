import time


def quickSort1(array, lt, rt):
    if lt < rt:
        pos = lt
        pivot = array[rt]
        for i in range(lt, rt):
            if array[i] <= pivot:
                array[i], array[pos] = array[pos], array[i]
                pos += 1
        array[rt], array[pos] = array[pos], array[rt]
        quickSort1(array, lt, pos-1)
        quickSort1(array, pos+1, rt)
    return array


def quickSortWithLeftPivot(array, lt, rt):
    if lt < rt:
        pos = lt + 1
        pivot = array[lt]
        for i in range(lt+1, rt+1):
            if array[i] <= pivot:
                array[i], array[pos] = array[pos], array[i]
                pos += 1
        array[lt], array[pos-1] = array[pos-1], array[lt]
        quickSort1(array, lt, pos-2)
        quickSort1(array, pos, rt)
    return array
array1 = [6, 36, 1, 5, 21, 15]

print(quickSortWithLeftPivot(array1, 0, len(array1)-1))


def quickSort2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quickSort2(left_side) + [pivot] + quickSort2(right_side)

array1 = [6, 36, 1, 5, 21, 15]
assert quickSort1(array1, 0, len(array1)-1) == [1, 5, 6, 15, 21, 36]
assert quickSort2(array1) == [1, 5, 6, 15, 21, 36]

def quickSort3(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quickSort3(array, start, right-1)
    quickSort3(array, right+1, end)
    return array

array1 = [6, 36, 1, 5, 21, 15]
assert quickSort3(array1, 0, len(array1)-1) == [1, 5, 6, 15, 21, 36]

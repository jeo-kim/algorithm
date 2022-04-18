def insertionSort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array


array1 = [1, 5, 3, 7, 22, 42, 77, 21, 83, 58, 6, 23, 67, 32, 4, 9]
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 10, 18, 19, 20]

assert insertionSort(array1) == [1, 3, 4, 5, 6, 7, 9, 21, 22, 23, 32, 42, 58, 67, 77, 83]
assert insertionSort(array2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 18, 19, 20]


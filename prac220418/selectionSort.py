array1 = [7, 5, 4, 2, 6, 1, 8, 3, 9]

def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

assert selectionSort(array1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
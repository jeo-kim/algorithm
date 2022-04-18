def mergeSort(array, lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2

        mergeSort(array, lt, mid)
        mergeSort(array, mid+1, rt)

        p1 = lt
        p2 = mid + 1
        tmp = []

        while p1 <= mid and p2 <= rt:
            if array[p1] < array[p2]:
                tmp.append(array[p1])
                p1 += 1
            else:
                tmp.append(array[p2])
                p2 += 1

        if p1 <= mid:
            tmp = tmp + array[p1:mid+1]
        if p2 <= rt:
            tmp = tmp + array[p2:rt+1]

        for i in range(len(tmp)):
            array[lt+i] = tmp[i]

    return array

def mergeSortAgain(array, lt, rt):
    if lt < rt:
        mid = (lt + rt) // 2

        mergeSortAgain(array, lt, mid)
        mergeSortAgain(array, mid+1, rt)

        p1 = lt
        p2 = mid + 1
        tmp = []

        while p1 <= mid and p2 <= rt:

            if array[p1] < array[p2]:
                tmp.append(array[p1])
                p1 += 1
            else:
                tmp.append(array[p2])
                p2 += 1

        if p1 <= mid:
            tmp = tmp + array[p1:mid+1]
        if p2 <= rt:
            tmp = tmp + array[p2:rt+1]

        for i in range(len(tmp)):
            array[lt+i] = tmp[i]

    return array
array1 = [14, 5, 33, 2, 9, 4, 20]
print(mergeSortAgain(array1, 0, len(array1)-1))




#
#
# array1 = [14, 5, 33, 2, 9, 4, 20]
# print(mergeSort(array1, 0, len(array1)-1))

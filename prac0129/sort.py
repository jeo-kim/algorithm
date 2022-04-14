list = [4, 6, 2, 9, 1]
#
# def selectionsort(lst):
#     iters = len(lst) - 1
#     for iter in range(iters):
#         minimun = iter
#         for cur in range(iter + 1, len(lst)):
#             if lst[cur] < lst[minimun]:
#                 minimun = cur
#
#         if minimun != iter:
#             lst[minimun], lst[iter] = lst[iter], lst[minimun]
#
#     return lst
#
# print(selectionsort(list))


def insertionsort(lst):
    # 0번째 요소는 이미 정렬되어있으니, 1번째 ~ lst(len)-1 번째를 정렬하면 된다.
    for cur in range(1, len(lst)):
        # 비교지점이 cur-1 ~ 0(=cur-cur)까지 내려간다.
        for delta in range(1, cur + 1):
            cmp = cur - delta
            if lst[cmp] > lst[cmp + 1]:
                lst[cmp], lst[cmp + 1] = lst[cmp + 1], lst[cmp]
            else:
                break
    return lst

print(insertionsort(list))
def DFS(L, weight):
    if L == len(nums):
        if weight >= 1:
            possible_set.add(weight)
        return
    else:
        weight -= nums[L]
        DFS(L+1, weight)
        weight += nums[L]
        DFS(L+1, weight)
        weight += nums[L]
        DFS(L+1, weight)


if __name__ == "__main__":

    nums = [ 1, 5, 7 ]
    S = 13
    possible_set = set()
    result_list = []
    DFS(0, 0)

    for i in range(1, S+1):
        if i not in possible_set:
            result_list.append(i)


    print(result_list)  # 출력 >> [9, 10]

def DFS(L, starting_i, now_sum):
    global count
    if L == k:
        if now_sum % 6 == 0:
            count += 1
        return
    else:
        for i in range(starting_i, len(nums)):
            DFS(L+1, i+1, now_sum+nums[i])

if __name__ == "__main__":

    nums = [2, 4, 5, 8, 12]
    k = 3
    n = 6
    count = 0
    DFS(0, 0, 0)

    print(count)
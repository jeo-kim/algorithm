def solution(numbers, target):
    count = 0
    def DFS(L, S):
        nonlocal count
        if L == len(numbers):
            if S == target:
                count += 1
            return
        else:
            DFS(L+1, S + numbers[L])
            DFS(L + 1, S - numbers[L])
    DFS(0, 0)

    return count

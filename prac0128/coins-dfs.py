coins = [8, 9, 11, 12, 23, 15, 17]

each_sum = [0] * 3

minimum = 2147000000
def DFS(L):
    global minimum
    global each_sum
    if L == len(coins):
        isValid = True
        for each in each_sum:  # 세 사람이 가진 총액은 서로 달라야 한다는 조건을 충족시키기 위한 검사
            if each_sum.count(each) > 1:
                isValid = False
        if isValid:
            diff = max(each_sum) - min(each_sum)
            if diff < minimum:
                minimum = diff
        return

    else:
        for i in range(3):
            each_sum[i] += coins[L]
            DFS(L + 1)
            each_sum[i] -= coins[L]
            # 이게 내가 자주 계획단계에서 놓치는 것! 재귀에서 빠져나올 때는 내가 방금 칸에 더했던 것을 다시 빼줘야 한다.

DFS(0)
print(minimum)

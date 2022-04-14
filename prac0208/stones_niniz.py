stones1 = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]

def solution(stones, k):
    answer = 0
    tmp = [0]
    n = len(stones)
    stones = stones + tmp
    while True:
        count = 0
        for i in range(0, n+1):
            if stones[i] == 0 and stones[i+1] == 0:
                count += 1

            if stones[i] != 0:
                stones[i] -= 1






    return answer
def solution(money):
    n = len(money)
    tmp = [0]
    money = tmp + money

    # 최대 돈 액수를 구하기 위한 다이나믹 테이블
    # 앞 뒤로 한 칸씩 더 만들어줘서 0을 두면 인덱스 에러 없이 사용하기 위한, 무의미한 가장자리를 만들어줄 수 있다.
    dy = [0]*(n+2)

    # 첫 집은 털기로 결정한 경우.
    # 뒤에서부터 인접한 것을 건너서 해당 집을 털 경우의 가능한 최대 액수를 기록해가는 과정
    # n 번째 집은 털 수 없으므로 for 범위에 미포함
    dy[1] = money[1]
    for i in range(3, n):
        dy[i] = max(dy[i-2], dy[i-3]) + money[i]

    # 1차후보 선발
    candidate1 = max(dy)

    # 마지막 인덱스를 선택한 경우에 대한 최대 돈 액수 구하기 위해 다이나믹 테이블 다시 초기화.
    dy = [0] * (n+2)

    # 마지막 집은 털기로 결정한 경우.
    # 뒤에서부터 인접한 것을 건너서 해당 집을 털 경우의 가능한 최대 액수를 기록해가는 과정
    # 1 번째 집은 털 수 없으므로 for 범위에 미포함
    dy[n] = money[n]
    for j in range(n-2, 1, -1):
        dy[j] = max(dy[j+2], dy[j+3]) + money[j]

    # 2차 후보 선발
    candidate2 = max(dy)

    # 두 경우(첫 집을 터는 경우, 마지막 집을 터는 경우) 중 더 큰 값으로 답 제출
    answer = max(candidate1, candidate2)
    return answer


# solution([91,90,5,7,5,7])

print(solution([1,2,3,1]), 4)
print(solution([1,1,4,1,4]), 8)
print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
print(solution([1000,1,0,1,2,1000,0]), 2001)
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([1,2,3]), 3)
print(solution([91,90,5,7,5,7]), 104)
print(solution([90,0,0,95,1,1]), 185)
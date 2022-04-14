import sys

# 입력값 받기
N = int(sys.stdin.readline().rstrip())
reqs = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().rstrip())

# 이분탐색을 시작할 초기 범위 설정
lt = 0
rt = max(reqs)
answer = 0

# 상한선에 따른 예산 총액 반환하는 함수
def how_much(limit):
    total = 0
    for req in reqs:
        if req > limit:
            total += limit
        else:
            total += req
    return total

# 이분탐색
while lt <= rt:
    mid = (lt+rt)//2
    # 설정한 mid 값을 상한선으로 했을 때, 예산 총액이 얼마인지 확인
    # 그 금액이 가능한 예산 범위 내에 있다면, 잠정 답안으로 반영하고,
    # lt를 mid 우측으로 옮겨서 더 큰 값 중에서 mid 를 검토하도록 한다.
    if how_much(mid) <= M:
        answer = max(answer, mid)
        lt = mid+1
    # 예산 범위를 넘었다면, 더 적은 값 중에서 mid 를 검토하도록 한다.
    else:
        rt = mid-1

print(answer)


import sys

k, n = map(int, sys.stdin.readline().split())
lines = []

for _ in range(k):
    line = int(sys.stdin.readline().rstrip())
    lines.append(line)

# 이분탐색을 시작할 초기 범위 설정
lt = 1
rt = max(lines)

# 상한선에 따른 예산 총액 반환하는 함수
def how_many(length):
    total = 0
    for line in lines:
        pieces = line//length
        total += pieces
    return total

answer = 0

# 이분탐색
while lt<=rt:
    mid = (lt+rt)//2
    if how_many(mid) >= n:
        answer = max(answer, mid)
        lt = mid+1
    else:
        rt = mid-1

print(answer)



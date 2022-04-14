import sys

# 입력값 받기
N = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().split()))

# 고정점이 될 수 있는 범위 초기 설정
left = 0
right = N-1

# 궁금한 점 : 남병관 튜터님 코드에선 hi = N 이고, hi를 낮출 때 hi = mid
# 그렇게 할 때 더 효율성이 더 좋은 점이 있나?

checked = False
while left <= right:
    # mid 로 불러온 인덱스와, 인덱스의 값이 같다면 고정점 발견한 것
    mid = (left+right)//2
    if a[mid] == mid:
        checked = True
        break
    elif a[mid] > mid:
        right = mid-1
    elif a[mid] < mid:
        left = mid+1

# 고정점 발견 없이 while 끝났다면 -1 출력
if not checked:
    print(-1)
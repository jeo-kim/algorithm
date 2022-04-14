# N = 4
# M = 7
# trees = [20, 15, 10, 17]
import sys

# 입력값 받기
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

# 이분탐색을 시작할 초기 범위 설정
lt = 0
rt = max(trees)
answer = 0

# 절단기 높이를 설정했을 때 얻어낼 수 있는 나무의 총 길이 구하는 함수
def how_long(length):
    total = 0
    # 나무 높이를 돌면서, 절단기 높이보다 높다면, 잘렸을 때 길이를 총 길이에 더해간다.
    for tree in trees:
        if tree > length:
            total += (tree-length)
        else:
            continue
    return total

# 절단기 높이의 최적값을 찾아가는 이분탐색
while lt <= rt:
    mid = (lt+rt)//2
    if how_long(mid) >= M:
        # 원하는 길이만큼 얻어낼 수 있는 절단기 세팅을 발견할 때마다 최댓값인지 봐서 갱신
        answer = max(answer, mid)
        lt = mid+1
    else:
        rt = mid-1

print(answer)

import collections
import sys

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().split()))

# 이분탐색을 할 대상이 될 A를 정렬
A.sort()
# 존재여부를 기록할 리스트(1 or 0으로)
answers = []
# B의 앞 요소부터 꺼내기 위한 큐
que = collections.deque(B)

# 더이상 꺼내 볼 B 요소가 없을 때까지
while len(que) > 0:
    # 꺼낸 B 요소가 타겟
    target = que.popleft()
    # 탐색 범위 설정
    lt = 0
    rt = len(A)-1
    # 타겟을 A에서 발견했는지 신호를 줄 boolean 변수
    exist = False
    # 이분탐색
    while lt <= rt:
        mid = (lt+rt)//2
        # 발견하면 존재여부리스트에 1추가, 발견 신호보내놓고, 이분탐색 while 문 종료
        if A[mid] == target:
            answers.append(1)
            exist = True
            break
        elif A[mid] < target:
            lt = mid + 1
        elif A[mid] > target:
            rt = mid - 1
    # A 다 탐색했는데 발견 신호 못 받았다면 존재여부리스트에 0 추가
    if not exist:
        answers.append(0)

for answer in answers:
    print(answer)

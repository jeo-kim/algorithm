# 문제 조건들 및 그에 따른 주의점들
# 조건1 ) 문자열 비교시(head) 대소문자 구분을 하지 않는다.
# ==> 일괄적으로 lower 해서 비교
# 조건 2) HEAD 가 동일하다면 ==> NUMBER 의 숫자 순 정렬
# 조건 2+) 숫자 맨 앞의 0은 무시 ** 내가 한참동안 잘못 이해했던 조건.
#           ==> 0을 삭제해서는 안 된다!
#               처음부터 연속된 5자리를 0이 차지하는 00000123이라면, 00000까지 NUMBER 로 인정하고, 처리만 0으로 해주는 것.
# 조건 3) HEAD, NUMBER 같은 경우 입력 순서대로 정렬
#           ==> 입력 순서도 인지하고 있어야 하기 때문에, i도 보관해준다.

import heapq
import re

def solution(files):
    # for 문 돌릴때마다 사용할 n(파일 개수)
    n = len(files)

    # 답을 위한 리스트
    answer = []

    # 우선순위에 따라 pop 해줄 heapq 로 사용할 리스트
    heap = []

    for i, file in enumerate(files):

        # 문자열 오름차순 비교를 위해 소문자로 바꾼다.
        lower = file.lower()

        # re 모듈을 사용해서 숫자덩어리가 처음 등장하는 부분을 추출한다.
        number = re.findall('\d+', lower)[0]

        # 숫자 덩어리의 첫 숫자가 문자열에서 등장하는 인덱스 위치를 잡아서, num_start 라는 변수에 담는다.
        num_start = lower.index(number[0])

        # 숫자 시작되는 인덱스 전까지 잘라서 head 로 삼기
        head = lower[:num_start]
        # 숫자 덩어리에서 5번 인덱스 직전까지만 자르기
        # (NUMBER 에 대한 인지방식이 숫자 등장부터 연속된 5자리까지이므로)
        num = int(number[:5])
        # 우선순위가 높은 순서대로, head > num > i(입력된 인덱스)
        heapq.heappush(heap, (head, int(num), i))

    for _ in range(n):
        head, num, idx = heapq.heappop(heap)
        answer.append(files[idx])

    return answer


# solution(files1)
# solution(files2)
# solution(files4)
# solution(files2)
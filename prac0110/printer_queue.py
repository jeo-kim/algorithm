import heapq
# 힙을 사용해보자.
# 최소값부터 / 혹은 최댓값을 맨 앞에 가져다 줄 수 있는 자료구조/ 정렬 방식. (이진트리)

### 서로 같은 값이 있을 때는 pop 할 순서를 컨트롤 하기가 어렵네.
### 문제가 되는 case 119111 .. (0번째 1의 pop 순서를 2로 출력해줌)
cases = int(input())

for _ in range(cases):
    n, target_idx = map(int, input().split( ))
    # 횟수와, 찾고자 하는 문서의 인덱스를 받아온다.
    nums = list(map(int, input().split( )))

    heap = []

    for idx, num in enumerate(nums):
        heapq.heappush(heap, (-num, num, idx))
        # 파이썬 내장 힙은 최소 힙만 지원한다고 함(우선순위(?) 최소값부터 제거할 수 있음)
        # 그걸 최대 힙으로 활용하려면 num 의 부호를 바꾸어서, 그걸 우선순위로 적용하면 됨. ( -num )
        # 인덱스를 기억해두어야 함..!

    count = 1
    while heap:
        a, b, c = heapq.heappop(heap)
        if c == target_idx:
            print(count)
            break
        count += 1


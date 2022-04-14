import collections
import heapq

def solution(priorities, location):
    # 타겟 location 의 문서가 몇 번만에 출력되었는지 count 해가는 변수
    answer = 0

    # 입력 순서를 지키고 있는 데큐
    q1 = collections.deque()
    # 우선순위 높은 것을 꺼내기 위한 heapq 로 사용할 리스트
    q2 = []

    # 입력된 우선순위들을 두 개의 큐에 넣어준다. 단 우선순위는 부호반전하여 넣는다. (최대힙처럼 사용하기 위해)
    for i, priority in enumerate(priorities):
        doc = (-priority, i)
        q1.append(doc)
        heapq.heappush(q2, doc)

    # 두 개의 큐에서 맨 앞에 있는 값의 우선순위를 비교하며 같을 경우, 해당 문서를 처리
    # 처리할 때마다 answer +=1 하고, 만약 처리한 문서의 인덱스가 타겟인 location 과 같다면 반복문 종료
    # 같지 않다면 다시 우선순위를 나타내는 큐는 변동이 아예 없고, 입력순서 지키는 큐에서는 꺼낸 값을 맨 뒤에 append
    while True:
        cur = q1.popleft()
        if cur[0] == q2[0][0]:
            answer += 1
            heapq.heappop(q2)
            idx = cur[1]
            if idx == location:
                break
        else:
            q1.append(cur)

    return answer


## any() 함수를 사용하는 방식도 가능! heapq도 사용했던 것 보다 공간은 더 적게 쓰는 것 같은데, 아마 시간은 좀 더 걸리겠지..?
import collections
def solution(priorities, location):
    que = collections.deque()
    for i, priority in enumerate(priorities):
        que.append((i, priority))

    answer = 0
    while True:
        cur = que.popleft()
        if any(cur[1] < x[1] for x in que):
            que.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                break

    return answer
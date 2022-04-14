import heapq
def solution(operations):

    heap1 = []  # 최솟값을 뽑아내기 위한 heap1
    heap2 = []  # 최댓값을 뽑아내기 위한 heap2

    for oper in operations:
        c, n = oper.split()
        n = int(n)

        if c == "I":
            heapq.heappush(heap1, n)
            heapq.heappush(heap2, -n)

        elif c == "D":
            # 어느 하나라도 비어있다면 삭제 명령 무시(heap1과 heap2 원소개수는 늘 동기화되므로 하나만 봐도 된다)
            if len(heap1) == 0:
                continue
            else:
                # 최솟값 삭제 명령이면, 자료 그대로 넣었던 heap1에서 pop 한다.
                # 그 값의 부호반전된 값을 반대편 heap 에서도 삭제
                if n == -1:
                    now_min = heapq.heappop(heap1)
                    heap2.remove(-now_min)
                # 최댓값 삭제 명령이면, 자료의 부호를 바꾸어 넣었던 heap2에서 pop한다.
                # 그 값의 부호반전된 값을 반대편 heap 에서도 삭제
                elif n == 1:
                    now_max = heapq.heappop(heap2)
                    heap1.remove(-now_max)

    # 모든 원소가 삭제되어서 힙이 비어있다면, 문제 요구에 따라 0,0 으로 리턴
    if len(heap1) == 0:
        return [0, 0]
    # 비어있지 않다면, 최대와 최소를 각각의 힙으로부터 pop 해서 제출 (heap2의 경우 부호반전해야 원래 자료값)
    else:
        max = -heapq.heappop(heap2)
        min = heapq.heappop(heap1)
        return [max, min]
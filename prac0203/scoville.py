import heapq
def solution(scoville, K):
    answer = 0
    # 작은 값부터 뽑을 것이므로 heap 사용할 것.
    heap = []

    # 이미 최솟값이 K 보다 크거나 같다면 섞어볼 필요 없어서 0회를 return
    if min(scoville) >= K:
        return 0

    # 최소힙을 지원하는 파이썬 heapq 를 사용하여  push
    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])

    # 최소가 K 이상이 될 때까지 작은 아이들 2명 뽑아서 새로운 조합 만들어보는 반복작업
    while True:
        # 종료조건 1) 2개도 안 남았다!(0개, 또는 1개)
        # 그런데 그나마 뽑아봤더니 K보다 작다면 주어진 조합에서는 아무리 섞어도 K를 넘길 수 없었던 것이므로 -1 리턴
        if len(heap) < 2:
            if heapq.heappop(heap) < K:
                answer = -1
            break

        # 종료조건 2) 가장 작은 아이를 뽑았다. 그랬는데, K 이상이라면 더 섞어 볼 필요는 없음.
        first = heapq.heappop(heap)
        if first >= K:
            break

        # 두 번째로 작은 아이도 뽑아서 new 를 만들어주고 heapq 에 append, 섞은 횟수가 늘었으니 answer +=1
        second = heapq.heappop(heap)
        new = first + 2*second
        heapq.heappush(heap, new)
        answer += 1

    return answer

# scoville = [1, 2, 3, 9, 10, 12]
scoville = [1, 1, 100]
K = 7


solution(scoville, K)
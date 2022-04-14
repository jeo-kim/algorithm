import heapq


def solution(scoville, K):

    heap = []
    heapq.heappush(heap, scoville)
    print()
    min_scoville = heapq.heappop(scoville)
    count = 0

    if min_scoville >= K:
        return 0

    while min_scoville >= K:
        count += 1
        second = heapq.heappop(scoville)
        new = min_scoville + second * 2
        heapq.heappush(heap, new)
        min_scoville = heapq.heappop(scoville)

    print(count)





    answer = 0
    return answer

solution([1, 2, 3, 9, 10, 12], 1)
# [1, 2, 3, 9, 10, 12]	 k = 7
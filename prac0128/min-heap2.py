# min-heap
# 0 일때는 "꺼내고"
# 다른 값이면 "넣어라"

import heapq
import sys

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    val = int(sys.stdin.readline())
    if val == 0:
        if len(heap) == 0:  # 아직 넣어준 게 없어서 heap 길이가 0이라면
            # 0을 출력한다.
            print(0)
        else:  # 넣어준 게 있다면
            # 힙에서 맨 꼭대기(루트) 값을 꺼낸다(heappop)
            print(heapq.heappop(heap))
    else:
        # 0 이 아닌 입력일 경우 > 그 값을 힙에 넣는다(heappush)
        heapq.heappush(heap, val)

# max-heap
# 0 일때는 "꺼내고"
# 다른 값이면 "넣어라"

# import heapq
# import sys

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    val = int(sys.stdin.readline())

    # 꺼내라는 명령이 떨어졌을 때
    if val == 0:

        if len(heap) == 0:  # 아직 넣어준 게 없어서 heap 길이가 0이라면
            # 0을 출력한다.
            print(0)
        else:  # 넣어준 게 있다면
            # 힙에서 맨 꼭대기(루트) 값을 꺼낸다(heappop)
            # 그런데 사실 입력해줄 때 "큰수"가 "작은 수"로 인식되게끔 하려고 부호를 바꿔 넣었기 때문에
            # 출력할 때 부호를 다시 바꿔서, 처음 입력할 때의 값의 상태로 보여주도록 한다.
            print(-(heapq.heappop(heap)))

    else:
        # 0 이 아닌 입력일 경우 > 그 값을 힙에 넣는다(heappush)
        # 기본적으로 최소힙을 지원하므로,
        # 입력할 때 부호를 바꿔서 넣는다.
        # 그러면 7, 5, 1  각각이 -7, -5, -1 이 되니까
        # 사실 가장 큰 수 였던 7이 가장 작은 수로서 들어가고
        # 나중에 힙에서 꺼낼 때, 가장 작은 수이므로 우선순위를 가지고 먼저 나온다.
        (heapq.heappush(heap, -val))



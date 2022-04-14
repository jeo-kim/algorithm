from collections import deque

result = []
import sys

input = sys.stdin.readline().split()

c_queue = deque()
for i in range(int(input[0])):
    c_queue.append(str(i + 1))

target = int(input[1])
now_turn = 0;

while len(c_queue) > 1 and c_queue:
    print(c_queue)
    now_turn += 1

    # 타켓이 아니니깐 맨 오른쪽으로
    if now_turn < target:
        c_queue.append(c_queue.popleft())
    # 타켓이니깐 데큐에서 제거하고 result에 삽입
    elif now_turn == target:
        result.append(c_queue.popleft())
        now_turn = 0;

result.append(c_queue.popleft())

print("<", ', '.join(result), ">", sep="")  # 결과 출력

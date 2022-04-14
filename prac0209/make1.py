import collections
import sys

n = int(sys.stdin.readline())
que = collections.deque([(n, 0)])

while True:
    num, cnt = que.popleft()
    # 만들고자 하는 수인 1이 되면 몇 번의 연산이 사용되었는지 출력하고 while 종료
    if num == 1:
        print(cnt)
        break
    # 1 뺀 값, 연산 횟수 1추가해서 큐에 넣기
    sub1 = (num-1, cnt+1)
    que.append(sub1)

    # 3으로 나눌 수 있다면 3으로 나눈 값, 연산 횟수 1 추가해서 큐에 넣기
    if num%3 == 0:
        div3 = (num//3, cnt+1)
        que.append(div3)

    # 2로 나눌 수 있다면 2로 나눈 값, 연산 횟수 1 추가해서 큐에 넣기
    if num%2 == 0:
        div2 = (num//2, cnt+1)
        que.append(div2)


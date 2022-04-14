# 현재 값보다 앞으로 추가해야 할 값이 크면 push,
# 현재 값보다 앞으로 추가해야 할 값이 작으면 pop
import collections

nums = [4, 3, 6, 8, 7, 5, 2, 1]
deq = collections.deque(nums)

# deqAsStack = collections.deque()
# deqAsStack.appendleft(0)

# howManyTimesPushed = 0
#
# for i, num in enumerate(nums):
#     top = deqAsStack.pop()
#     deqAsStack.append(top)  # 계속 참조하려면... 다시 넣어줘야 할 것 같아서
#     if num > top:
#         # 작성하려는 수가 스택 꼭대기보다 큰 경우에는, 스택이 모자란 것이니 더 쌓아줘야 함.
#         for j in range(top+1, num+1):  # 현재 스택 꼭대기보다 큰 값부터, 지금 쌓으려는 num 까지 push
#             deqAsStack.append(j)
#
#         last = deqAsStack.pop()  # 스택의 top 을 반환
#         deq.append(last)  # deq 에 덧붙이기
#     else:
#         # 작성하려는 수가 스택 꼭대기와 동일한 경우에는, 스택꼭대기를 내어주기.
#         if num == top:
#             last = deqAsStack.pop()  # 그 꼭대기를
#             deq.append(last)
################################3
# list 대신 나중에 deque 로 바꾸기. (시간 복잡도 위해서)

stack1 = list()
stack2 = list()
stack3 = list()

stack3.append(0)

for num in nums:
    if num > stack3[-1]:
        while i in range(stack3[-1]+1 : num):




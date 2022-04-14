import collections


# def solution(bridge_length, weight, truck_weights):
#
#     # answer =  1 + (counter * bridge_length) + (sisters)
#     #
#     # stack = collections.deque()
#     # # stack.append(0)
#     # count = 1
#     # sisters = 0
#     #
#     # for i, truck in enumerate(truck_weights):
#     #     if sum(stack) + truck <= weight:  # 지금 이 친구가 들어와도 최대하중보다 작다면
#     #         stack.append(truck)
#     #
#     #     elif sum(stack) + truck > weight:
#     #         sisters += len(stack)-1
#     #         stack.clear()
#     #         count += 1
#     #         stack.append(truck)
#     #
#     # print("count= ", count, " sisters= ", sisters)
#     #
#     #


import collections
def solution(bridge_length, weight, truck_weights):
    waiting_trucks = collections.deque(truck_weights)
    bridge_queue = collections.deque([0] * bridge_length)
    count = bridge_length
    # while 문은 마지막에 있던 트럭이 딱 다리에 들어가자 마자 종료할 건데, 그러면 그 이후에 다리 길이만큼 시간이 더 흘러야 통과하니까.
    # 처음부터 다리길이를 시간의 초기값으로 두어보자.

    while len(waiting_trucks) != 0:
        count += 1
        bridge_queue.popleft()

        if sum(bridge_queue) + waiting_trucks[0] <= weight:
            bridge_queue.append(waiting_trucks.popleft())

        else:
            bridge_queue.append(0)

    return count



bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]  # count = 1

bridge_length1 = 2
weight1 = 10
truck_weights1 = [7,4,5,6]

bridge_length2 = 100
weight2 = 100
truck_weights2 = [10]  # count = 1 , sisters = 0



solution(bridge_length, weight, truck_weights)
solution(bridge_length1, weight1, truck_weights1)
solution(bridge_length2, weight2, truck_weights2)
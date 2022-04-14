import collections

def solution(bridge_length, weight, truck_weights):

    total_time = 1

    checked_dict = collections.defaultdict(list)  # 각 트럭 인덱스를 키로, 그것이 앞서서 포함된 적 있는지 여부 확인하는 딕셔너리

    for i in range(len(truck_weights)):
        sum = truck_weights[i]
        checked_dict[i].append(i)

        for j in range(i+1, len(truck_weights)):
            sum += truck_weights[j]
            if sum > weight:  # 그 다음 차 무게를 더했더니 촤대하중 넘었다면 # 그 다음 차로 j+1 하지 않아도 된다.
                break
            else:  #
                checked_dict[i].append(j)  # 나는 포함 된 적 있다고 알려주기.
                j += 1

    print(checked_dict)

    for key, with_list in checked_dict.items():
        # total_time += len(value)-1
        if key == 0:   # 처음 요소는 일단 다리 길이만큼 시간이 걸리고, 자신 뒤에 데려온 동생들 수만큼 시간을 더해준다.
            total_time += bridge_length
            total_time += (len(with_list) - 1)
        elif key not in checked_dict[key-1]:

                total_time += bridge_length
                total_time += len(with_list) - 1
        else:
            count = 0
            for idx in with_list:
                if idx not in checked_dict[key-1]:
                    count += 1
            total_time += count

    print(total_time)
    return total_time


bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

bridge_length1 = 2
weight1 = 10
truck_weights1 = [7,4,5,6]

bridge_length2 = 100
weight2 = 100
truck_weights2 = [10]



solution(bridge_length, weight, truck_weights)
solution(bridge_length1, weight1, truck_weights1)
solution(bridge_length2, weight2, truck_weights2)




        # big_list[i].append(truck_weights[i])  # 자신의 무게를 넣기.
        # now_sum = sum(big_list[i])    # 지금까지 무게 합하기
        # j = i+1  # 자기보다 뒤에 트럭 무게부터 검사 시작
        #
        # if now_sum + truck_weights[j] <= weight:  # 지금까지 더한 것(now_sum)에다가 그 다음거(j)를 더해도 최대하중보다 크지 않다면
        #     big_list[i].append(truck_weights[j])  # 커다란 리스트 속 i번째 아빠 리스트에다가 j번째 무게도 append 해준다.
        #     j += 1  # 그 다음 것도 계산해주어야 하니까

    # 숫자마다 돌면서, 다음 숫자랑 자기라


    #
    #
    #
    #
    #
    #
    # answer = 0
    # return answer
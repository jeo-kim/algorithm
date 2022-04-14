distance1 = 25
rocks1 = [2, 14, 11, 21, 17]
n1 = 2

def solution(distance, rocks, n):
    rocks.append(distance)
    # rocks 를 오름차순으로 정렬
    rocks.sort()

    # 가장 인접한 바위 사이의 거리가 주어졌을 때, 남겨두어야 하는 바위의 개수 이상으로 남길 수 있는지 판단해주는 함수
    def isOK(min_dis):
        nonlocal n
        nonlocal rocks
        prev = 0
        count = 0
        for i in range(0, len(rocks)):
            cur = rocks[i]
            dis = cur - prev
            if dis < min_dis:
                continue
            else:
                count += 1
                prev = cur

        if count >= len(rocks) - n:
            return True
        else:
            return False

    # 가장 인접한 바위 간의 거리로 가능한 범위를 정해두고
    # mid 조정해가는 이분탐색 진행
    start = 1
    end = distance
    answer = 0

    while start <= end:
        mid = (start+end)//2
        print(isOK(mid))
        if isOK(mid) is True:
            answer = max(answer, mid)
            start = mid + 1
        else:
            end = mid - 1

    return answer

solution(distance1, rocks1, n1)
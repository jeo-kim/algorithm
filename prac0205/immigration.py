def solution(n, times):
    answer = int(1e18)

    # mid 의 움직임에 따라 총 심사시간이 상정되면, 그 안에 몇 명까지 심사가능한지 구하는 함수
    # 이 값을 가지고 심사시간을 늘려야 할지 줄여도 될지 판단할 것
    def how_many(limit):
        total = 0
        # 각 심사위원이 걸리는 시간으로 총 심사시간을 나누어서 구한 각각의 몫들을 더한다.
        # 모든 심사위원이 빈틈없이 계속 사람을 받을 경우를 나타냄.
        for time in times:
            total += limit//time
        return total

    # 최소 1분, 최대는 모든 사람을 모든 심사위원이 동일하게 처리할 경우 걸릴 시간으로.
    lt = 1
    rt = (max(times) * n)//len(times) + 1

    # 이분탐색. mid 가 상정한 시간으로 하면 n명의 사람을 심사할 수 있는지 판단.
    # 적으면 심사시간을 늘리고(lt를 이동), 충분하면 심사시간을 줄여본다(rt 이동)
    while lt <= rt:
        mid = (lt+rt)//2
        if how_many(mid) >= n:
            answer = min(answer, mid)
            rt = mid - 1
        else:
            lt = mid + 1

    return answer








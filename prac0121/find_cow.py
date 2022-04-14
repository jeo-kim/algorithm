import collections
def findCow(start:int, destination: int, max_position: int):
    positions_que = collections.deque()
    positions_que.append(start)
    distance = [0] * (max_position + 1)
    distance[start] = 0
    checked = [0] *(max_position + 1)

    while positions_que:
        now = positions_que.popleft()
        if now == destination:
            break
        for next in (now-1, now+1, now+5):
            if 0 < next <= max_position:
                if checked[next] == 0:
                    positions_que.append(next)
                    checked[next] = 1
                    distance[next] = distance[now] + 1

    return distance[destination]

# 예제 확인 print(findCow(5, 14, 10000))
                    
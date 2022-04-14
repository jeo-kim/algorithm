qs = [
    [10, 5],
    [25, 12],
    [15, 8],
    [6, 3],
    [7, 4]
]

M = 20
res = 0

def DFS(level, start, time, score):
    global res
    # 제한 시간을 딱 맞춘 경우에는 현재 점수를 그대로 제출해서 기존 값과 비교하고 최댓값으로 갱신
    if time == M:
        res = max(res, score)
        return
    # 제한 시간을 넘긴 경우, 방금 전에 추가했던 점수를 뺀 값과 기존 값을 비교하고 최댓값으로 갱신
    if time > M:
        res = max(res, score - qs[start-1][0])
        return
    # 제한 시간이 남은 경우, 가능한 조합의 가지를 더 뻗어나가기
    else:
        for i in range(start, len(qs)):
            DFS(level+1, i+1, time+qs[i][1], score+qs[i][0])

DFS(0,0,0,0)
print(res)



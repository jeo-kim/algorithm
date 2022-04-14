import collections

orders = [
    [1, 4],
    [5, 4],
    [4, 3],
    [2, 5],
    [2, 3],
    [6, 2]
]

# 진입차수를 기록할 1차원 배열 마련 및 초기값 채우기
degree = [0] * len(orders)
for order in orders:
    degree[order[1]-1] += 1

# 진입차수 0이지만 이미 큐에 넣어서 처리한 아이들 중복 처리 안하도록
checked = [0] * len(orders)

# 진입차수가 0이 된 아이들을 순서대로 처리하기 위한 que
que = collections.deque()
for i, each in enumerate(degree):
    if each == 0:
        que.append(i+1)
        checked[i] = 1

# 순서대로 작업 출력할 리스트
res = []

while que:
    # 0이어서 들어와 있던 작업 꺼내서 처리
    prev = que.popleft()
    res.append(prev)
    # 방금 꺼낸 아이를 선행조건으로 갖고 있던 아이들의 차수 -= 1
    for order in orders:
        if order[0] == prev:
            degree[order[1]-1] -= 1
    # 이미 처리했던 아이들이 아니라면, 차수가 0이 된 아이들은 que 에 넣어주고, check 표시도 해준다.
    for i, each in enumerate(checked):
        if each == 0 and degree[i] == 0:
            que.append(i+1)
            checked[i] = 1

# 결과 출력
print(res)






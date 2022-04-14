n = 4
m = 4
map = [
    [0, 1, 2, 0],
    [1, 0, 2, 1],
    [0, 2, 1, 2],
    [2, 0, 1, 2]
]

# 집 좌표 리스트, 피자 좌표리스트 만들기
houses = []
pizzas = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            houses.append((i,j))
        if map[i][j] == 2:
            pizzas.append((i,j))

# 선택된 피자집의 조합을 담을 배열(좌표 자체가 아닌, 인덱스로 담을 것이기 때문에 정수인 0 으로 초기화 한 것)
cb = [0] * m

# res : 도시의 피자배달거리 -- 최솟값이 나올 때마다 갱신해서 최종 제출할 것
res = 2147000000

# DFS - 깊이 우선 탐색으로 m 개의 피자집 조합을 만들고, 그 경우들에 대한 도시의 피자배달 거리를 구한다.
def DFS(L, start):
    global cb
    global res
    # m 개의 피자집 조합이 완성되면, 그 조합 속 피자집들 중 각 집들에 대해 가장 가까운 피자집과의 거리를 구하고, 이를 합산하여 도시의 총 거리를 res 에 제시(?)
    # 조합이 만들어질 때마다 매번 총 배달거리가 제시될 텐데, 미리 제시된 값보다 작을 경우에만 갱신되도록 함.
    if L == m:
        sum = 0
        for j in range(len(houses)):
            x1 = houses[j][0]
            y1 = houses[j][1]
            dis = 2147000000
            for x in cb:
                x2 = pizzas[x][0]
                y2 = pizzas[x][1]
                dis = min(dis, abs(x1-x2)+abs(y1-y2))
            sum += dis

        if sum < res:
            res = sum

    else:
        for i in range(start, len(pizzas)):
            cb[L] = i
            DFS(L+1, i+1)

DFS(0, 0)
print(res)
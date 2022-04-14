import sys
# n 은 도시(정점) 수, m 은 간선 수
n, m = map(int, sys.stdin.readline().split())

# 2차원 배열 준비 (i 행에서 j 열로 가는데 드는 비용을 적을 곳)
dis = [["M"]*n for _ in range(n)]

# 입력된 연결 및 비용 정보 반영하기
for _ in range(m):
    i, j, price = map(int, sys.stdin.readline().split())
    dis[i-1][j-1] = price

# 자신을 도착지로 삼는 경로의 비용은 0으로 만들어두기
for i in range(n):
    for j in range(n):
        if i == j:
            dis[i][j] = 0

# k번째 도시마다, 각 도시를 경유대상으로 포함하여 고려할 경우, 최소 비용 다시 계산해가는 과정
for k in range(0, n):
    for i in range(n):
        for j in range(n):
            if dis[i][j] == "M":  # 기존 값이 "M" 인데
                if dis[i][k] != "M" and dis[k][j] != "M":  # 경유해서 계산한 값이 "M"이 아니면 경유한 비용으로 갱신
                    dis[i][j] = dis[i][k] + dis[k][j]
                else:  # 경유과정에도 "M" 이 끼어있으면 그냥 "M"
                    dis[i][j] = "M"
            else:  # 기존 값이 "M" 이 아닌데
                if dis[i][k] != "M" and dis[k][j] != "M":  # 경유과정에도 "M"이 없다면, 둘다 유효한 값이니까 대소비교해서 갱신
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
                else:  # 경유과정에 "M"이 끼어있다면 기존 값을 갱신할 필요 없이 넘어감.
                    continue


for line in dis:
    line = map(str, line)
    print(" ".join(line))



#
# 6 9
# 1 2 12
# 1 3 4
# 2 1 2
# 2 3 5
# 2 5 5
# 3 4 5
# 4 2 2
# 4 5 5
# 6 4 5
import sys

n = int(sys.stdin.readline().rstrip())
dy = [["M"]*n for _ in range(n)]

# 자신과의 거리는 0
for i in range(n):
    dy[i][i] = 0

# 입력 라인이 -1 -1로 종료를 알릴 때까지 연결 정보를 받아온다.
while True:
    i, j = map(int, sys.stdin.readline().split())
    if i == -1 and j == -1:
        break
    dy[i-1][j-1] = 1
    dy[j-1][i-1] = 1

# k 번째 친구를 경유하는 상황을 하나씩 추가해서 고려하면서, 최소 거리를 업데이트.
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dy[i][j] == "M":
                if dy[i][k] != "M" and dy[k][j] != "M":
                    dy[i][j] = dy[i][k] + dy[k][j]
                else:
                    continue
            else:
                if dy[i][k] != "M" and dy[k][j] != "M":
                    dy[i][j] = min(dy[i][j], dy[i][k] + dy[k][j])
                else:
                    continue

# 각 행마다 자신의 최대 거리를 기록
each_max = []
for i in range(n):
    each_max.append(max(dy[i]))

# 최대거리가 가장 적은 경우의 최대거리 -> 이는 곧 회장 후보의 점수
lowest = min(each_max)
# 회장 후보 점수를 가진 사람 수
count = 0
# 회장 후보 리스트
candidates = []

# 최저점을 가진 사람을 발견할 때마다 count 증가, 해당 인덱스에 1을 더해서 후보가 누구인지도 출력
for i, max in enumerate(each_max):
    if max == lowest:
        count += 1
        candidates.append(str(i+1))

print(lowest, count)
print(" ".join(candidates))





print()

#
# print(dy)



# 2 1
# 3
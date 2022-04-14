qs = [
    [10, 5],
    [25, 12],
    [15, 8],
    [6, 3],
    [7, 4]
]

M = 20

# 동적으로 기입해갈 2차원 배열 준비
dy = [[0]*(M+1) for _ in range(len(qs) + 1)]

for i in range(1, len(qs)+1):
    time = qs[i-1][1]
    score = qs[i-1][0]
    #
    for j in range(time, M+1):
        dy[i][j] = max(dy[i-1][j], dy[i-1][j-time] + score)

print(f"{M}동안 풀 수 있는 최대 점수는 {dy[len(qs)][M]}")




# 1차원 배열 준비
dy = [0] * (M+1)

for i in range(len(qs)):
    time = qs[i][1]
    score = qs[i][0]
    for j in range(M, time-1, -1):
        dy[j] = max(dy[j], dy[j-time]+score)

print(f"{M}동안 풀 수 있는 최대 점수는 {dy[M]}")

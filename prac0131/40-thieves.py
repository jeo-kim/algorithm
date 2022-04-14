n = 3
stones = [
    [3, 3, 5],
    [2, 3, 4],
    [6, 5, 2]
]

record = [[0] * n for _ in range(n)]
record[0][0] = stones[0][0]

# for i in range(n):
#     for j in range(n):
#         # 0행의 경우 참고할 위칸은 없으므로, 바로 왼쪽 칸만 참고하면 된다.
#         # 그리고 j까지 0인 경우는 시작점이고 답을 미리 정해놓았으므로 따로 계산하지 않고 pass
#         if i == 0:
#             if j == 0:
#                 pass
#             else:
#                 record[i][j] = record[i][j-1] + stones[i][j]
#
#         else:
#             # 0 행은 아니면서 0열인 곳에 있는 칸은, 바로 위쪽 칸만 참고하면 된다.
#             if j == 0:
#                 record[i][j] = record[i-1][j] + stones[i][j]
#             # 맨 위의 행와 맨 왼쪽의 열이 모두 아닌 칸들의 경우, 왼쪽과 위에 인접한 칸들로부터 그들의 기록을 살펴보고
#             # 그 중 더 적은 에너지를 들인 경로를 택할 것이므로, 더 적은 기록에 자신의 높이까지 더하여 자신까지 오는데 필요한 최소 에너지를 기록한다.
#             else:
#                 record[i][j] = min(record[i-1][j], record[i][j-1]) + stones[i][j]
#
# print(record[n-1][n-1])

n = 3
stones = [
    [3, 3, 5],
    [2, 3, 4],
    [6, 5, 2]
]

record = [[0] * n for _ in range(n)]
record[0][0] = stones[0][0]

def DFS(i, j):
    # 0행 0열의 경우 바로 자신의 높이만큼만 리턴해준다.
    if i == 0 and j == 0:
        return stones[0][0]
    # 0행의 경우, 자신의 왼쪽 칸만 참고하여, 그 친구에 자신의 높이를 더한만큼 리턴한다.
    elif i == 0:
        record[i][j] = DFS(i, j-1) + stones[i][j]

    # 0열의 경우, 자신의 위쪽 칸만 참고하여, 그 친구에 자신의 높이를 더한만큼 리턴한다.
    elif j == 0:
        record[i][j] = DFS(i-1, j) + stones[i][j]

    else:
    # 0행도 0열도 아닌 경우, 자신의 왼쪽과 위의 칸이 제시할 최소 에너지들 중 더 min 인 값을 채택하고, 자신의 높이를 더하여 리턴한다.
    # 혹시라도 왼/위에 대해서 미리 구해둔 계산 결과가 있다면, 그 칸에 대해서는 재귀 호출하지 않고 record 에서 참고하여 return.
        if record[i-1][j] != 0 and record[i][j-1] != 0:
            record[i][j] = min(record[i-1][j], record[i][j-1]) + stones[i][j]

        elif record[i-1][j] != 0:
            record[i][j] = min(record[i-1][j], DFS(i, j-1)) + stones[i][j]

        elif record[i][j-1] != 0:
            record[i][j] = min(DFS(i-1, j), record[i][j-1]) + stones[i][j]

        else:
            record[i][j] = min(DFS(i-1, j), DFS(i, j-1)) + stones[i][j]

    return record[i][j]


print(DFS(n-1, n-1))


# m = 5
# n = 4
# puddles = [[3,2], [1,4]]

m = 4
n = 3
puddles = [[2,2]]


def solution(m, n, puddles):
    INF = int(1e9)
    graph = [[INF]* (m+1) for _ in range(n+1)]
    already = [[-1]* (m+1) for _ in range(n+1)]

    for puddle in puddles:
        row, col = puddle[1], puddle[0]
        already[row][col] = INF

    count = 0
    def DFS(i, j):
        nonlocal count
        if i==1 and j==1:
            count += 1
            return 0
        elif already[i][j] == -1:
            if i == 1:
                left = DFS(i, j-1)
                already[i][j] = left + 1
            elif j ==1:
                top = DFS(i-1, j)
                already[i][j] = top + 1
            else:
                left = DFS(i, j - 1)
                top = DFS(i - 1, j)
                already[i][j] = min(left, top) + 1
        return already[i][j]

    DFS(n, m)
    print(count)


    answer = (already[n][m]-1) % 1000000007
    return answer

solution(m, n, puddles)
# print(already[n][m])
# print()
# for i in range(n+1):
#     print(already[i])

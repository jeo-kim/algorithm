class Solution(object):
    def solveNQueens(self, n):
        visited = [-1] * n
        answers = []

        def DFS(self, L):
            nonlocal n
            nonlocal visited
            nonlocal answers
            if L == n:
                grid = [['.']* n for _ in range(n)]
                for v, i in enumerate(visited):
                    grid[i][v] = "Q"
                result = []
                for row in grid:
                    result.append(''.join(row))
                    print(row)
                answers.append(result)
                return

            else:
                for col in range(n):
                    visited[L] = col
                    isPossible = True
                    for passed_row in range(L):
                        if visited[L] == visited[passed_row] or L-passed_row == abs(visited[L]-visited[passed_row]):
                            isPossible = False
                    if isPossible:
                        DFS(L+1)

        DFS(0)
# print(solveNQueens(4))
    # print(answers)

sol = Solution()
print(sol.solveNQueens(4))

# def nqueen(n):
#     visited = [-1] * n
#     answers = []
#
#     def DFS(L):
#         if L == n:
#             grid = [['.']* n for _ in range(n)]
#             for v, i in enumerate(visited):
#                 grid[i][v] = "Q"
#             result = []
#             for row in grid:
#                 result.append(''.join(row))
#                 print(row)
#             answers.append(result)
#             return
#
#         else:
#             for col in range(n):
#                 visited[L] = col
#                 isPossible = True
#                 for passed_row in range(L):
#                     if visited[L] == visited[passed_row] or L-passed_row == abs(visited[L]-visited[passed_row]):
#                         isPossible = False
#                 if isPossible:
#                     DFS(L+1)
#
#     DFS(0)
#     print(answers)
#
#
# nqueen(5)

# assert nqueen(4) == [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
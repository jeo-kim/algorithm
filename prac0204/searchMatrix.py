# class Solution(object):
#     def searchMatrix(self, matrix, target):
#
#         if not matrix:
#             return False
#
#         row = 0
#         col = len(matrix[0])
#
#         while row <= len(matrix) -1 and col >= 0:
#             if target == matrix[row][col]:
#                 return True
#             # 타겟이 작으면 왼쪽으로 이동
#             elif target < matrix[row][col]:
#                 col -= 1
#             # 타겟이 크면 아래로 이동
#             elif target > matrix[row][col]:
#                 row += 1
#
#         return False

class Solution(object):
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)
matrix1 = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]


class Solution(object):
    def searchMatrix(self, matrix, target):

        for i, row in enumerate(matrix):
            left = i  # 0행의 경우라면 0번 칸, 1행의 경우 1번 칸
            right = len(row)-1

            # 각 행(가로)에 대한 이진탐색
            while left <= right:
                mid = (left+right)//2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    right = mid-1
                elif row[mid] < target:
                    left = mid+1
            # 이 앞의 좌우 탐색에서 이미 [i][i]는 봤으니까 상하 탐색의 시작점은 그보다 한 개 이후부터했는데
            # 시간이 절반정도나 줄었다.
            top = i+1
            bottom = len(matrix)-1

            # 각 열(세로)에 대한 이진탐색
            while top <= bottom and i <= len(row)-1:
                # 행 수와 열 수가 같지 않은 경우도 있어서 while 이 돌아가는 조건 2번을 추가함
                middle = (top+bottom)//2
                if matrix[middle][i] == target:
                    return True
                elif matrix[middle][i] > target:
                    bottom = middle-1
                elif matrix[middle][i] < target:
                    top = middle+1

        return False



sol = Solution()
print(sol.searchMatrix(matrix1, 32))
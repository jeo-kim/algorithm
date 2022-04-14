# class Solution(object):
#     dx = [0, 0, -1, 1]  # dx 와 dy 의 i 번째들을 동시에 참조하면 (위, 아래, 좌, 우 이렇게 이동할 수 있음)
#     dy = [-1, 1, 0, 0]
#
#     def DFS(self, grid, x, y):
#         if grid[x][y] != 1:
#             return
#
#         grid[x][y] = 0
#         for i in range(4):
#             xx = x + self.dx[i]
#             yy = y + self.dy[i]
#             if 0 <= xx < len(grid[0]) and 0 < yy < len(grid) and grid[xx][yy] == 1:
#                 self.DFS(grid, xx, yy)
#
#     def numIslands(self, grid):
#
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     self.DFS(grid, i, j)
#                     print(i, j)
#                     count += 1
#
#         print(count)

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        # dx 와 dy 의 i 번째들을 동시에 참조해서 상하좌우 이동할 것.
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]



        def DFS(x,y):
            if grid[x][y] == "0":
                return

            else:
                grid[x][y] = "0"
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]

                    if 0<=new_x<len(grid) and 0<=new_y<len(grid[0]) and grid[new_x][new_y] == "1":
                        DFS(new_x, new_y)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    DFS(i, j)
                    count += 1

        return count



grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

sol = Solution()
sol.numIslands(grid1)
sol.numIslands(grid2)
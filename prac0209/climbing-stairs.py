class Solution:
    def climbStairs(self, n: int) -> int:

        # bottom-up 으로 동적으로 기록해갈 배열
        dy = [0] * (n+1)
        # 작고 확실한 출발점
        dy[0] = 1
        dy[1] = 1
        # 전칸, 전전칸까지 올 수 있던 방법수를 합하여 해당 칸에 기록
        for i in range(2, n+1):
            dy[i] = dy[i-1] + dy[i-2]

        return dy[n]


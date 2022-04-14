# m = 8
# n = 8
# puddles = [[2,6], [4, 3], [8, 7], [1, 8]]

m = 4
n = 3
puddles = [[2,2]]

def solution(m, n, puddles):
    # 각 칸에 이르기 위한 최단거리의 가지 수 기록할 동적 배열
    dy = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            isPuddle = False
            # i, j가 물웅덩이라면 거기로 갈 수 있는 방법 수는 0
            for puddle in puddles:
                if puddle[1] == i+1 and puddle[0] == j+1:
                    dy[i][j] = 0
                    isPuddle = True
                    break
            # 물웅덩이가 아니라면
            if not isPuddle:
                # 시작점이라면 확실하게 1을 리턴 (작고 확실한 출발점)
                if i == 0 and j == 0:
                    dy[i][j] = 1
                # 1행이라면 왼쪽 칸까지 온 방법 수 그대로 물려받고
                elif i == 0:
                    dy[i][j] = dy[i][j-1]
                # 1열이라면 위의 칸까지 온 방법 수 그대로 물려받고
                elif j == 0:
                    dy[i][j] = dy[i-1][j]
                # 그렇지 않다면 위의 칸과 왼쪽 칸 각각까지 올 수 있는 방법 수 더해서 자기 칸에 기록
                else:
                    dy[i][j] = dy[i-1][j] + dy[i][j-1]

    answer = (dy[n-1][m-1]) % 1000000007
    return answer



solution(m, n, puddles)
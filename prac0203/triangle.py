triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    # 자주 사용할 숫자 변수로
    n = len(triangle)

    # 각 칸에 이르면서 만들 수 있는 최대합을 기록할 다이나믹 배열 준비
    dy = []
    for i in range(n):
        row = [0] * (i+1)
        dy.append(row)

    # 작고 확실한 시작점
    dy[0][0] = triangle[0][0]

    for j in range(1, n):
        for k in range(j+1):
            if k == 0:
                dy[j][k] = dy[j-1][k] + triangle[j][k]
            elif k == j:
                dy[j][k] = dy[j-1][k-1] + triangle[j][k]
            else:
                dy[j][k] = max(dy[j-1][k-1], dy[j-1][k]) + triangle[j][k]

    answer = max(dy[n-1])
    return answer

solution(triangle)
# 예시 자료
bricks = [
    [25, 3, 4],
    [4, 4, 6],
    [9, 2, 3],
    [16, 2, 5],
    [1, 5, 2]
]

# 무게 기준 내림차순 정렬하기
bricks.sort(key=lambda x: x[2], reverse=True)

# 각 벽돌에 대해, 자신이 꼭대기에 있을 경우 가능한 최대 높이를 기록할 배열 준비
max_h = [0] * len(bricks)

# 맨 앞에 있는 벽돌은 가장 무거운 친구라서, 자신이 꼭대기에 있을 경우 가능한 상황은, 자기 자신만 있는 경우이다.
# 그래서 가능한 최대 높이도 자신의 높이임을 미리 단정가능하다.
max_h[0] = bricks[0][1]

for i in range(1, len(bricks)):
    # 자신보다 밑면이 넓은 친구가 없을 경우, 디폴트 최대 높이는 자기 자신의 높이이므로 my_max 를 아래와 같이 초기화
    my_max = bricks[i][1]
    for j in range(0, i):
        if bricks[j][0] > bricks[i][0]:
            if my_max < max_h[j]+bricks[i][1]:
                my_max = max_h[j]+bricks[i][1]

    max_h[i] = my_max

print(f"쌓을 수 있는 최대 높이는 {max(max_h)} 입니다.")


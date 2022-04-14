import collections
# 테스트 재료 : 사과 밭
apple_field = [
    [10, 13, 10, 12, 15],
    [12, 39, 30, 23, 11],
    [11, 25, 50, 53, 15],
    [19, 27, 29, 37, 27],
    [19, 13, 30, 13, 19]
]
# 코드 시작
# BFS 를 위한 Queue 준비
que = collections.deque()

# 탐색 출발 전 세팅
n = len(apple_field)
total = 0
total += apple_field[n//2][n//2]
que.append((n//2, n//2))
L = 0
check = [[0]*n for _ in range(n)] # 방문 여부 체크할 중첩리스트
check[n//2][n//2] = 1 # 가운데는 체크 해둠
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# BFS
while True:
    if L == n//2:
        break
    que_size = len(que)
    # 처음에 강사분이 이렇게 que_size 를 미리 변수로 지정해두고 아래 for in range( ) 에 사용하시는 게 의아했다.
    # 그냥 바로 range(len(que)) 하면 안 되는건가? 했다.
    # 물론 이게 코드를 움직일 때는 range( )에 사용한 len(que)는 엄밀히 말해 for문 밖에 있으니까,
    # 나름 그 값은 for 문 내부 작업에 영향 받지 않았던 듯 싶고 결과를 출력하는 데 문제는 없었던 것 같다.
    # 하지만 가독성 차원에서(??) 한 레벨에서 다룰 que 의 개수를 고정시켜주는 게 좋은 것 같다.
    # 안그러면 아래에 출력해본 결과 for 의 밖에서 선언한 que_size 는 한 레벨 동안은 안정적인 반면, len(que)는 계속 변화가 반영된다.
    for i in range(que_size):
        print("L= ", L,"que_size= ", que_size, " len(que)= ", len(que) )
        tmp = que.popleft()
        for j in range(4):
            new_x = tmp[0] + dx[j]
            new_y = tmp[1] + dy[j]
            if check[new_x][new_y] == 0:
                check[new_x][new_y] = 1
                total += apple_field[new_x][new_y]
                que.append((new_x, new_y))

    L += 1
print(total)
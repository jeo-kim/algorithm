import collections

maze = [
    [0,0,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,0,0,1,0,0,0],
    [1,1,0,1,0,1,1],
    [1,1,0,1,0,0,0],
    [1,0,0,0,1,0,0],
    [1,0,1,0,0,0,0],
]

distance = [[0]*7 for _ in range(7)]
que = collections.deque()
que.append((0,0))
maze[0][0] = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while que:
    if distance[6][6] != 0:
        # que 가 소진될 때까지 돌지 않고, 어떤 가지가 목표지점에 도달해서 거리 정보를 갱신한 순간 while 종료하면 어떨까?
        # 이게 조금이라도 시간을 덜 쓰는 방법이 맞으려나
        # 도착지까지의 거리 리력
        print(distance[6][6])
        break

    tmp = que.popleft()
    for i in range(4):
        new_x = tmp[0] + dx[i]
        new_y = tmp[1] + dy[i]
        if 0<=new_x<7 and 0<=new_y<7 and maze[new_x][new_y]==0:
            maze[new_x][new_y] = 1
            distance[new_x][new_y] = distance[tmp[0]][tmp[1]] + 1
            que.append((new_x, new_y))
# 예외
if distance[6][6] == 0:
    print(-1)
# # 원하는 결과 값
# print(distance[6][6])


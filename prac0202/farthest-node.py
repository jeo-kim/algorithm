import heapq

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, edge):
    # 최단거리 테이블 초기화
    distance = [int(1e9)] * (n+1)
    distance[1] = 0

    # 전체 연결 정보 테이블
    con = [[int(1e9)] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        con[i][i] = 0

    for each in vertex:
        start = each[0]
        end = each[1]
        con[start][end] = 1
        con[end][start] = 1


    print(con[1][1:])

    # 방문 여부 확인용 테이블 (0: 미방문, 1: 방문)
    visited = [0] * (n+1)

    # 미방문 노드 중 최단 거리 뽑아내기 위한 heap
    heap = []

    # 경유할 노드 하나씩 뽑아서
    for _ in range(n):
        m = int(1e9)
        # 노드 1에서
        for i, each in enumerate(con[1][1:]):
            if visited[i] == 1:
                continue
            else:
                m = min(m, each)
        idx = con[1].index(m)
        visited[idx] = 1
        for j in range(1,n+1):
            con[1][j] = min(con[1][j], con[1][idx] + con[idx][j])

    print(con[1])





    return

solution(n, vertex)
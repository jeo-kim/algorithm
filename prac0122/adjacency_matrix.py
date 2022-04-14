def make_adjacency_matrix(nodes: int, connects_list: list):

    graph = [[0]*(nodes+1) for _ in range(nodes+1)]
    #  앞의 한 칸 0번이 추가로 만들어지지만 인덱스를 노드 번호로 바로 사용하기 위해 요렇게 준비시켜준다.

    for connect in connects_list:
        from_node = connect[0]  # 시작 노드(from) 뽑고
        to_node = connect[1]  # 도착 노드(to) 뽑고
        weight = connect[2]  # from -> node 로의 가중치 뽑고
        graph[from_node][to_node] = weight
        # 준비해둔 행렬에 정보를 넣는다. (from 행(시작노드)에서 to 열(도착노드)까지 가중치 정보를 행렬 칸에 넣는 것.)

    for i in range(1,nodes+1):  # 1번부터, 마지막 노드 번호까지 (이 문제에서 들어온 노드 번호는 순차적이므로 이렇게 표현이 가능)
        # 각각 자신의 행에서 제공하는 정보, 즉 각 열과의 연결관계를 뽑기 위해 1번부터 마지막 노드번호까지의 열을 순회한다.
        for j in range(1, nodes+1):
            print(graph[i][j], end=" ")  # i 행에서 j 열에 어떤 가중치로 연결되었는지 정보를 출력해보기.
        print()  # 표처럼 보기 위해 줄바꿈이 되도록

nodes = 6
connects_list = [
    [1,2,7],  # 1번 노드에서 2번 노드로 7만큼의 가중치로 연결된다는 의미.
    [1,3,4],
    [2,1,2],
    [2,3,5],
    [2,5,5],
    [3,4,5],
    [4,2,2],
    [4,5,5],
    [6,4,5]
]

make_adjacency_matrix(nodes, connects_list)
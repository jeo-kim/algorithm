INF = int(1e9)

n, m = map(int, input().split())
dis = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dis[i][i] = 0

# 자신보다 성적이 높은 아이들(자기와 대소비교가 가능한 아이들)이라고 입력에 주어진 것을 반영
for _ in range(m):
    a, b = map(int, input().split())
    dis[a][b] = 1

# k 라는 커서가 하나씩 노드들을 돌면서, 매개물의 역할을 해본다.
for k in range(1, n+1):
    # a 와 b 가 대소비교 가능할까? 를 생각해주는 것. 만약 매개물을 통해서라도 대소비교가 가능하다면 INF 가 아닌 값으로 갱신.
    for a in range(1, n+1):
        for b in range(1, n+1):
            dis[a][b] = min(dis[a][b], dis[a][k] + dis[k][b])

result = 0
# 모든 노드들을 매개물로 삼아봐서 테이블 갱신이 완료되었으니


for cur in range(1, n+1):
    cnt = 0
    for node in range(1, n+1):
        # 각 노드들마다 - 자기노드(cur)행에서 특정 노드(node) 보다 점수 낮다는 정보가 있거나,
        # 아니면 특정노드(node)행에서 자기노드(cur)보다 점수가 낮다는 정보가 있다면,
        if dis[cur][node] != INF or dis[node][cur] != INF:
            # 그 노드와는 대소비교가 가능한 것. 자기노드행에서 그런 아이들 개수를 세어줌.
            cnt += 1
    # 그렇게 대소비교가능한 친구가 모든 노드개수와 같다면, 자신의 순위를 정확히 아는 것.
    # 순위를 아는 노드를 발견했으니 result +=1
    if cnt == n:
        result += 1
print(result)
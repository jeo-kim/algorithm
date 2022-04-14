import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):

        # 초기화에 사용할 큰 수
        INF = int(1e8)

        # 각 노드 간 간선과 간선에 해당하는 시간(가중치)에 대한 정보를 2차원 배열에 반영
        graph = [[] for _ in range(n+1)]
        for time in times:
            graph[time[0]].append((time[1], time[2]))

        # 각 노드에 이르는 최소시간을 적어놓을 1차원 배열
        mins = [INF] * (n+1)

        def dijkstra(start):

            # 최소 시간인 경로부터 뽑기 위해 heapq 준비
            que = []
            heapq.heappush(que, (0, k))

            # 시작점으로 가는 데 걸리는 시간 0으로 초기화
            mins[k] = 0

            # 하나씩 최소비용인 것 que 에서 뽑아서 그 다음 인접 노드를 향한 경유지로서 고려해가는 반복작업
            while que:
                # 해당노드에 가는데 걸리는 (시간, 해당 노드) 꺼내서 unpack
                time, now = heapq.heappop(que)
                # 이미 최소 시간 테이블에 now 노드에 이르는 시간이 더 짧게 기록되었다면
                # 지금 발견한 경로는 무시.
                if mins[now] < time:
                    continue

                # 지금 발견한 경로가 무시할만 한 것이 아니어서 if 를 타지 않고 여기 왔다면
                # now 와 인접한 node, 그리고 now 에서 거기까지 가는데 걸리는 시간(d_time)을 꺼내온다.
                for node, d_time in graph[now]:
                    # 새로 산정하는 소요 시간은, now 까지 오는데 들었던 time 과 now ~ node 로 가는데 드는 d_time 의 합
                    cost = time + d_time
                    # 새 소요시간이 기존에 기록된 node 까지의 소요시간보다 적다면, 최소시간 테이블 갱신하고,
                    # 지금 node 까지 이르는 이 경로도 heap 에 넣어 다음번에 참고할 수 있도록 한다.
                    if cost < mins[node]:
                        mins[node] = cost
                        heapq.heappush(que, (cost, node))

        # 신호보내는 노드 k 를 시작으로 다익스트라 실행
        dijkstra(k)

        # 0번 인덱스는 사용하지 않으므로 배제하고 최댓값 구하기
        answer = max(mins[1:])

        # 한 번도 경유 가능한 경로를 거치지 않아서 갱신되지 않은 INF 를 가졌다면 도달 불가한 경우가 있는 것
        if answer >= INF:
            return -1
        # 모든 노드가 갱신된 적 있다면 최댓값인 answer 리턴
        else:
            return answer


#
#
#
# sol = Solution()
# sol.networkDelayTime(times, n, k)
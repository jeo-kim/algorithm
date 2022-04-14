import collections

# rooms = [[1,3],[3,0,1],[2],[0]]
# rooms = [[1],[2],[3],[]]
rooms = [[2],[],[1]]

class Solution(object):
    result = False
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # 방 인덱스별로 키들의 리스트를 값으로 갖는 딕셔너리 생성
        my_dict = collections.defaultdict(list)
        for i, keys in enumerate(rooms):
            my_dict[i] = keys

        # 지금까지 획득한 키들의 set
        my_keys = set()

        # 각 방별로 방문했는지 체크하기 위한 배열, 0번째방에서 출발하므로 1로 체크해두기
        visited = [0] * len(rooms)
        visited[0] = 1

        def DFS(L, room):
            # 0에서 시작된 L 이 len(rooms)-1에 이르렀다면
            # 방 개수만큼 Level 을 진행했다면 방을 모두 방문한 셈이므로 result = True 로 해주고 return
            if L == len(rooms)-1:
                self.result = True
                return

            else:
                # 현재 방 room 의 키들을 가져와서, my_keys 에 추가
                for key in my_dict[room]:
                    my_keys.add(key)
                # 나의 키들중 하나씩 뽑아서, 방문하지 않은 방이고 지금 있는 방이 아닌 키가 있을 때 거기로 들어간다.
                for key in list(my_keys):
                    if visited[key] == 0 and key != room:
                        visited[key] = 1
                        DFS(L+1, key)
        DFS(0, 0)
        return self.result

sol = Solution()
print(sol.canVisitAllRooms(rooms))




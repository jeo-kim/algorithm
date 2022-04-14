import collections
import copy


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        res = []
        result_box = []
        airport_set = set()
        copied_tickets = copy.deepcopy(tickets)

        my_dict = collections.defaultdict(list)

        for i, ticket in enumerate(tickets):
            # for j in range(2):
            #     airport_set.add(tickets[i][j])

            my_dict[ticket[0]].append(ticket[1])

        for key, value in my_dict.items():
            value.sort()


        print(my_dict)
        sorted_list = sorted(list(airport_set))

        def DFS(airport):
            print("지금 DFS에서 출발지인 공항은 :", airport)

            if len(my_dict[airport]) == 0:
                if len(copied_tickets) == 0:
                    print("이제 티켓 남은 것 없다.DFS에서 출발지인 공항은 :", airport)
                    print(res)
                    result_box.append(res[:])
                    return
                else:
                    return

            # # 종료 조건
            # if len(copied_tickets) == 0:
            #     print("이제 티켓 남은 것 없다.DFS에서 출발지인 공항은 :", airport)
            #     print(res)
            #     result_box.append(res[:])
            #     return

            else:
                if len(my_dict[airport]) != 0:  # 지금 공항에서 갈 수 있는 다른 공항이 있다면
                    # res.append(airport)

                    print(f"{airport}에서 갈 수 있는 공항들 : {my_dict[airport]}")
                    for next_airport in my_dict[airport]:

                        DFS(next_airport)
                        res.append(airport)
                        # copied_tickets.remove([airport, next_airport])
                else:
                    print(f"{airport}에서 갈 수 있는 공항이 없습니다.")



        DFS("JFK")



            # 반복할 일
            # else:
            #     # for candidate in sorted_list:
            #     # 리스트 순서대로 돌되,






                # for next_airport in sorted_list:
                #     if [airport, next_airport] in copied_tickets:
                #         # print("지금 airport는 [", airport, "]에서 이동할 다음 공항은 [", next_airport, "]")
                #
                #         res.append(airport)
                #
                #         copied_tickets.remove([airport, next_airport])
                #
                #         DFS(next_airport)
                #     # else:
                #         # print(" ----- 지금 airport인 [", airport,"]에서 이동할 다음 공항은 없습니다!")


        # DFS("JFK")
        # print(result_box[0])
        # return result_box[0]


# tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
tickets3 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

sol = Solution()
# sol.findItinerary(tickets1)
# sol.findItinerary(tickets2)
sol.findItinerary(tickets3)
#
# print(sol.findItinerary(tickets1))

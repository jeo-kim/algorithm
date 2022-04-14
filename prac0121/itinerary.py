import collections

tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# ["JFK","MUC","LHR","SFO","SJC"]

tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
# ["JFK","ATL","JFK","SFO","ATL","SFO"]

tickets3 = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
# ["JFK","NRT","JFK","KUL"]

tickets4 = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
# ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]

# ["JFK","NRT","JFK","KUL"]

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        res = [0] * (len(tickets)+1)

        my_dict = collections.defaultdict(list)

        for i, ticket in enumerate(tickets):
            my_dict[ticket[0]].append(ticket[1])

        for key, value in my_dict.items():
            value.sort()

        used_tickets = []


        def DFS(L: int, now: str):
            if L == len(tickets):
                res[L] = now
                print(res)
                return

            if len(my_dict[now]) < 1:
                # used_tickets.
                return

            else:
                # used_tickets.append([res[L-1], now])
                if now in my_dict[res[L-1]]:
                    my_dict[res[L-1]].remove(now)

                for candidate in my_dict[now]:
                    # if candidate in my_dict[now]:
                    # # if [now, candidate] not in used_tickets:
                    res[L] = now
                    # used_tickets.append([now, candidate])
                    DFS(L+1, candidate)
                    # used_tickets.clear()


        DFS(0, "JFK")
        print(f"res는 ==>", res)
        return res










sol = Solution()
# sol.findItinerary(tickets1)
# sol.findItinerary(tickets2)
# sol.findItinerary(tickets3)
sol.findItinerary(tickets4)

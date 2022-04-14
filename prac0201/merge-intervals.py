
intervals = [[1,4],[0,2],[3,5]]

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # start 가 빠른 아이들 순으로 정렬
        intervals.sort()

        i = 0
        while True:
            # 마지막 인덱스보다 하나 앞일 때까지만 while 작용
            if len(intervals)-1 > i:
                # i 번째 자식 리스트의 end 값이 i+1 번째 리스트의 start 보다 같거나 크다면 병합
                if intervals[i][1] >= intervals[i+1][0]:
                    # 병합본의 시작은 i의 start, 끝은 i와 i+1 자식 리스트 중 더 큰 end 값.
                    merged = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
                    # i 번째에 병합본을 넣고
                    intervals[i] = merged
                    # i+1 번째는 지운다.
                    del intervals[i+1]

                # 현재 지켜본 i 와 i+1 이 병합 불가였다면, i +=1 을 하여 다음 두 인접 리스트를 비교하게 한다.
                else:
                    i += 1
            else:
                break

        print(intervals)
        return intervals


sol = Solution()
sol.merge(intervals)


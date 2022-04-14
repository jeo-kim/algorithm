import collections

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # 큐로 만들기.
        temp_que = collections.deque(temperatures)

        # 하나씩 빼고, 비교를 위한 다른 리스트에 넣기
        another_que = collections.deque()

        # 결과를 담을 리스트
        result_que = collections.deque()

        # temperatures 의 길이만큼
        i = 0
        while i < len(temperatures):
            crnt_last = temp_que.pop()

            # 체크 여부 확인
            checked = False

            # print(crnt_last) # 뒤에서부터 잘 나오고 있다.
            # [73, 74, 75, 71, 69, 72, 76, 73]
            # ==> [73, 76, 72, 69, 71, 75, 74, 73]
            if len(another_que) != 0:  # 적어도 맨 끝의 자료라도 옮겨 둔 이후에는
                for idx, elem in enumerate(another_que):  # 그 another que 에서 돌면서 자기보다 큰게 있나 확인.
                    if crnt_last < elem:  # 어떤 원소가  자기보다 크다면
                        # 그 원소의 인덱스 번호 +1 (자기보다 몇 번째 뒤인지)을 결과큐에 추가
                        result_que.appendleft(idx + 1)
                        # 나는 검사를 하였으니 another que 에도 옮겨 주기.
                        another_que.appendleft(crnt_last)
                        # 나는 나보다 더 큰 아이를 another que에서 찾았다라는 의미로 checked = True 로.
                        checked = True
                        # 자기 보다 큰 아이를 한번이라도 만났으면 더 이상 another_que 를 돌아볼 필요가 없음.
                        print(crnt_last, idx + 1)
                        break

                if checked is False:
                    result_que.appendleft(0)
                    another_que.appendleft(crnt_last)

            else:  # 첫 번째 (즉 temperatures 의 마지막 아이가 검사할 때만 거치는 곳)
                result_que.appendleft(0)
                another_que.appendleft(crnt_last)

            i += 1

        return list(result_que)


sol = Solution()

temperatures1 = [73,74,75,71,69,72,76,73]  # len 8
temperatures2 = [30,40,50,60]
temperatures3 = [30,60,90]

# sol.dailyTemperatures(temperatures)
print(sol.dailyTemperatures(temperatures1))
print(sol.dailyTemperatures(temperatures2))
print(sol.dailyTemperatures(temperatures3))


### O(n) 의 풀이. 리트코드 soloZ
class Solution:
    def dailyTemperatures(self, T: list[int]) -> list[int]:
        n, right_max = len(T), float('-inf')  # 오른쪽에서의 최댓값 (?) 은 음의 무한대로 초기화 해두고.
        res = [0] * n  # 일단 개수 n, 각 원소 값은 0들로 갖는 리스트로 결과 담을 곳 준비.
        for i in range(n-1, -1, -1):  # 마지막 인덱스 부터, 0번까지. 거꾸로 돌아가면서.
            t = T[i]  # t는 주어진 자료형의 i번째.
            if right_max <= t:  # 만약 우측 최댓값이 지금 자료값보다 같거나 작다면,
                right_max = t
                # 우측 최댓값은 지금것으로 업데이트. (예를 들어 첫 아이(마지막 인덱스)가 들어올 때는 right_max 가 음의 무한대니까 당연히 더 작을 것)
                # 더 큰 값이 없다면, res 에 대해 변화가 없다 => 즉 초기화 해둔 그대로, 작용할까 싶었던 인덱스의 값은 0 이다.

            else:  # 우측 최댓값이 지금 자료값보다 크다면,
                days = 1
                while T[i+days] <= t:
                    # (언제에서야 나보다 큰 값이 나오지?)를 찾기 위한 while문
                    # T[]보다 t가 같거나 큰 경우에 실행 == t(현재 값)보다 비교값이 커지면 종료
                    days += res[i+days] # <=== 신기한 부분.
                    # 최초 while 문 입장시에는
                    # 초기화된 days = 1 이니까, 처음에는 바로 다음날인 T[i+1]를 확인
                    # 그리고 그 다음 비교할 날짜는 며칠 후까지 갈까?! 를 의미하는 days 를 업데이트해주는데
                    # 비교하려는 뒤의 자료들에 대해서는 res(며칠 걸리는지 결과 리스트)에 값이 다 주어진 상태(거꾸로 for문을 돌고 있으니까)
                    # 그래서 비교하려는 인덱스의 res 값을 확인하면, 그 날로부터 며칠을 더 지나야 그 값보다 커지는지를 알 수 있음
                    # 즉 처음에는 days = 1 로 시작해서 바로 다음날과 비교하지만,
                    # 그다음에는 그 비교하고 있는 날의 인덱스가 알려주는 거다 아래처럼
                    # "적어도 이만큼 가야 나보다 큰 애가 나타나거든? 너도 더 큰 값을 만나려고 하는거잖아? 그럼 적어도 이만큼 뒤에서 검사해봐!"
                    # 즉 res 를 작성하는 와중에 이미 작성된 res 를 재참조까지 하고 있는 것...!!
                    # 아니 어떻게 이런 생각을 하는 거지.
                    # 그렇게 해서 방금 비교해본 친구가 알려준 걸 참고로 슝(물론 한칸만 갈 수도 있지만) T값 다시 검사해본다.
                    # 그걸 반복하다가 T[~]값이 드디어 현재 주인공인 t보다 커지는 순간에 while 문 종료.

                res[i] = days
                # days 가 어떤 값이길래 res[i]로 할당해줄 수 있는 건지 다시 생각해보면
                # days 는 "t가 방금 전까지 비교했던 res[i]들을 다 더한 값" + "1(초기화해두었던 값" 이니까
                # t 입장에서 며칠 후에야 자기보다 큰 값이 나오는지 적절하게 반영해준다.
                # (나보다 1은 큰 애부터 시작해서, 만난 아이들이 계속 "x"만큼 더 가렴, "y"만큼 더 가렴 , 이렇게 말한 셈인데
                # 초기값 1에다가 res[i+days](<-x, y 같은 애들)를 업데이트한 거니까 현재 t보다 얼마나 뒤에 있는지 잘 계산한 셈..
                # 그래서 이렇게 완성된 days 값을 현재 t의 결과인 res[i]로 내보내준 것.
        return res

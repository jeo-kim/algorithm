import collections

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        candidates = []  # 중복없이 슬라이싱된 단어들 담을 리스트
        char_list = list(s)  # 문자열 검사하면서 앞에부터 자유롭게 pop(0)하기 위해 리스트로 바꾸어봄. (데큐가 나은나?)

        # 예외
        # (1) 완전 아무 값도 안 들어올 때
        if len(s) == 0:
            return 0
        ###############
        # (2) 빈 공간오면 return 1...
        # " ", "   " --> 1 이어야 하는데 이 상황은 어떻게 경우로 만들어주지?

        # (3) 중복이 하나도 없을 때
        count_list = []
        for char in s:
            count_list.append(s.count(char))

        if max(count_list) == 1:
            print(s, len(s))
            return len(s)
        ############################

        while char_list:   # char_list 가 존재하는 동안. (계속 맨 앞을 지워줄 것이기 때문에 끝까지 검사하면 while 종료됨)

            my_dict = collections.defaultdict(int)  # 각 문자가 몇 번 등장했는지 세주기 위한 딕셔너리
            #   예 { "a" : 1,
            #        "b" : 1 }  이런 모양으로 만들거긴 한데
            # char_list 가 변화할 때마다 새로 만들어 줄 것 ( 알파벳 등장 횟수를 다시 세준다.)

            # char_list = [ 'a', 'b', 'c', .. ]
            for i, char in enumerate(char_list):

                # key 는 문자 자신으로, 그에 대한 값은 +1 한다. ( default dict 이므로 초기값은 0)
                my_dict[char] += 1

                # 그런데 이 문자가 2번 등장했다면
                if my_dict[char] > 1:
                    # 이 문자의 인덱스인 i 직전까지 char_list 를 잘라내고 후보단어리스트(candidates)에 추가한다.
                    candidates.append(char_list[:i])
                    # 중복 단어가 이미 등장했으니 기존의 char_list 를 더 볼 필요는 없다.
                    break

                if i == len(char_list)-1:  # 중복된 것 없이 주어진 문자열의 끝까지 갔다면?
                    # print(char_list)
                    candidates.append(char_list)
                    # "aab"에서 ["a", "b"] 가 안 되는 문제가 있었다.
                    # 그 이유는 여기서 참조한 char_list 를  64 line 에서 pop(0) 할 때 이미 candidates 에 추가한 char_list 에도 반영이 돼서.
                    # 딕셔너리를 순회하는 이 for 문 뿐만 아니라, char_list 를 새로 생성하는 while 문도 break 해주어야 했다.

                    break

            if i == len(char_list) - 1:
                break


            # char_list 에서 맨 앞 요소를 제거한 채 다시 검사를 해야 한다.
            # "abacde" 라는 단어가 있다면, 처음 후보로 등록된 친구는 "ab" 지만,
            # a를 없애고 다시 봐야 더 긴 "bacde" 를 발견할 수 있을테니까.


            char_list.pop(0)

        # 후보리스트에 있는 단어들의 길이를 보기 위한 리스트 준비
        # 근데 단어 추출이 필요한 게 아니라 최댓값만 내보내주면 되는 거라면, set 을 사용해도 되겠다
        length_li = []

        # 예시 s1 = "abcabcbb" 의 경우
        # 후보자들 리스트 : [['a', 'b', 'c'], ['b', 'c', 'a'], ['c', 'a', 'b'], ['a', 'b', 'c'], ['b', 'c'], ['c', 'b'], ['b'], []]
        for candidate in candidates:
                length_li.append(len(candidate))

        # length_li = [3, 3, 3, 3, 2, 1, 1] 이렇게 될 것.
        # 이 중에서 최댓값인 숫자의 인덱스를 가져와서 target_i로 지정
        target_i = length_li.index(max(length_li))

        # 후보자들 리스트에서 target_i 번째 있는 리스트를 문자열로 전환.
        word = "".join(candidates[target_i])

        # 선택된 단어와 그 길이를 출력
        print(word, len(word))

        return len(word)


sol = Solution()

s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = "abc"
s5 = "aab"  # 맨 끝에 >> a

#
sol.lengthOfLongestSubstring(s1)
sol.lengthOfLongestSubstring(s2)
sol.lengthOfLongestSubstring(s3)
sol.lengthOfLongestSubstring(s4)
sol.lengthOfLongestSubstring(s5)

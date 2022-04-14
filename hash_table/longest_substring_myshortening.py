import collections

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        candidates = []  # 중복없이 슬라이싱된 단어의 길이들 담을 리스트
        char_list = list(s)
        # 문자열 검사하면서 앞에부터 자유롭게 pop(0)하기 위해 리스트로 바꾸어봄. (데큐가 더 나으려나)
        # 예외 처리 1
        if len(s) == 0:
            return 0
        # 예외 처리 2
        count_list = []
        for char in s:
            count_list.append(s.count(char))

        if max(count_list) == 1:
            return len(s)

        while char_list:
            # 각 문자가 몇 번 등장했는지 세주기 위한 딕셔너리
            my_dict = collections.defaultdict(int)

            for i, char in enumerate(char_list):
                my_dict[char] += 1  # 이 문자가 2번 등장했다면
                if my_dict[char] > 1:
                    candidates.append(i) # i 직전까지 단어의 길이 >> 0 ~ (i-1) = i
                    break

                if i == len(char_list)-1: # 중복된 것 없이 주어진 문자열의 끝까지 갔다면
                    candidates.append(i+1)
                    # "aab"에서 ab 추출이 안 되는 문제가 있었다.
                    # 그 이유는 여기서 참조한 char_list 를  64 line 에서 pop(0) 할 때, 이미 candidates 에 추가한 char_list 에도 반영이 돼서.
                    # 딕셔너리를 순회하는 이 for 문 뿐만 아니라, char_list 를 새로 생성하는 while 문도 break 해주어야 했다.
                    break

            if i == len(char_list) - 1:
                break

            # char_list 에서 맨 앞 요소를 제거한 채 다시 검사
            char_list.pop(0)

        # 중복 없는 단어의 길이들의 리스트에서 최댓값 리턴
        return max(candidates)



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

import collections

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        candidates = []
        my_dict = collections.defaultdict(int)

        start = 0
        dupExist = False
        added = False
        for i, char in enumerate(s):
            # (1) 에서 더해졌다면, dict 가 클리어 되어야..
            if added:
                my_dict.clear()
                my_dict[s[i-1]] = 1
            my_dict[char] += 1
            #
            if i == len(s)-1 and my_dict[char] < 2:
                candidates.append(s[start:])

            for k, v in my_dict.items():
                if v > 1:  # 이러면 필요한 작업을 진행
                    dupExist = True
                    word = s[start:i]
                    if start != i: # 공백은 안나오게 하려고.
                        candidates.append(word)  ### 지점 (1)
                        added = True
                        start = i
                        break
                else:
                    added = False

        if not dupExist:
            return len(s)

        print(candidates)

        len_list = []
        for i, candidate in enumerate(candidates):
            len_list.append((len(candidate)))

        print(max(len_list))
        if len_list:
            return max(len_list)
        else:
            return 0


        #     # if len(candidate) == max(len())
        # print(candidates)

## 방금 중복되었던 것만 초기화하고 있구나..


sol = Solution()
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
sol.lengthOfLongestSubstring(s1)
sol.lengthOfLongestSubstring(s2)
sol.lengthOfLongestSubstring(s3)
sol.lengthOfLongestSubstring("au")
sol.lengthOfLongestSubstring("aab")
sol.lengthOfLongestSubstring("dvdf")


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        num_list = []

        for char in s:
            num_list.append(ord(char))

        num_set = set(num_list)
        only_one_list = [x for x in num_set]

        only_one_list.reverse()

        for i, num in enumerate(only_one_list):
            # 4 -> 3 -> 2 -> 1
            while num_list.count(num) >= 2:
                crnt_i = num_list.index(num)
                next = num_list[crnt_i + 1]
                if num >= next:
                    if num_list[i-1] < num and num_list[i-1]==num_list[i+1]:
                        if num < num_list[i+2]:
                            num_list.reverse()
                            num_list.remove(num)
                            num_list.reverse()
                    else:
                        num_list.remove(num)
                elif num < next:
                    num_list.reverse()
                    num_list.remove(num)
                    num_list.reverse()


        character_list = []

        for num in num_list:
            character_list.append(chr(num))

        return "".join(character_list)


sol = Solution()
print(sol.removeDuplicateLetters("cdadabcc"))
# print(sol.removeDuplicateLetters("bcabc"))
# print(sol.removeDuplicateLetters("ccacbaba"))
# print(sol.removeDuplicateLetters("abacb"))  # acb  ///abc
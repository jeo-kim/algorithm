# Input: s = "bcabc"
# Output: "abc"

# Input: s = "cbacdcbc"
# Output: "acdb"

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1 = []
        new_list = []

        now_max = False

        for char in s:
            list1.append(ord(char))
        once_set = set(list1)
        list2 = list(list1)
        mini = min(list2)
        print("mini!!!!", mini)
        print("mini!!!!", chr(mini))

        for i, num in enumerate(reversed(list1)): ### 큰 수부터 들어오게 하려고.
            print(list1.count(97))
            print("#####!!!", once_set)
            while num is max(once_set) and list1.count(num) > 1: ## 큰수가 딱 왔는데, 한 개 이상이다? 그럼
                if num is mini:                                         ## 최소값이 아니라면 통과하구
                    print(num, "##############", chr(num))
                    list1.reverse()
                    list1.remove(num)
                    list1.reverse()

                # 지울까 하는데 바로 뒤에 자기보다 큰 친구가 남아있을 때              ## 지우려고 하는데 혹시 나보다 큰 친구가 내 뒤에 있다면?
                if list1[list1.index(num)+1] > num:
                    list1.reverse()
                    list1.remove(num)
                    list1.reverse()


                else:
                    list1.remove(num)

            #
            # if list1.count(num) < 2:
            #     once_set.remove(num)
            # if now_max is True:
            #     once_set.discard(now_max)


        for number in list1:
            new_list.append(chr(number))
        result_word = "".join(new_list)

        return result_word

## 만약 지우려고 하는데 사이에 나보다 큰 아이가 있다면?! 그럼 뒤에꺼를 지워야 돼.


sol = Solution()
# print(sol.removeDuplicateLetters("cbacdcbc"))
# print(sol.removeDuplicateLetters("bcabc"))
print(sol.removeDuplicateLetters("cdadabcc"))
# a, b, c, d

# 중복되는 애들 중에서
# 제일 알파벳 뒷자리를 본다면
# 당연히 맨 앞에거는 우선적으로 빼야하지 않을까?..


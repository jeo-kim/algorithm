class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0:
            return []

        chars_at_digit = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }

        res_list = []
        res = ["@"] * len(digits)

        def DFS(L):
            if L == len(digits):
                word = "".join(res)
                res_list.append(word)
                return

            else:
                key_digit = digits[L]
                for char in chars_at_digit[key_digit]:
                    res[L] = char
                    DFS(L+1)

        DFS(0)
        return res_list


digits1 = "23"
sol = Solution()

sol.letterCombinations(digits1)
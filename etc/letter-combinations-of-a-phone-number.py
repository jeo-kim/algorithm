class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        numChar_dict = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','y','x','z']
        }

        for digit in digits:
            for i, letter in enumerate(numChar_dict[digit]):
                print(i, letter)




sol = Solution()

digits1 = "24"
sol.letterCombinations(digits1)

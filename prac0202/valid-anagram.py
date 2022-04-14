s = "anagram"
t = "nagaram"

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if sorted(list(s)) == sorted(list(t)):
            return True
        return False

sol = Solution()
sol.isAnagram(s, t)

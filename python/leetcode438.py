import os


class Solution:

    def __str__(self):
        return self.__hash__()

    def findAnagrams(self, s ,p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if s == "" or p == "":
            return 0





sp = Solution()
res = sp.findAnagrams("123", "")
print(res)

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        k = 0
        for i in reversed(range(len(s))):
            ret += (ord(s[i])-64) * (26 ** k)
            k += 1
        return ret
            
            
        
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        ans = []
        if num == 0:
            return '0'
        k = 0
        if num < 0:
            num = 2**32 + num
        while num>>k:
            ans.append(s[(num&(15<<k))>>k])
            k += 4
        ansStr = ''
        for c in reversed(ans):
            ansStr += c
        return ansStr
'''
这个题果然是easy的题，没看清楚题干，然后就把题目想复杂了……
'''

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        la, lb = len(a), len(b)
        if la != lb: return max(la,lb)
        if a != b: return la
        return -1
#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1.insert(' ',0)
        word2.insert(' ',0)
        l1, l2 = len(word1), len(word2)
        f = []
        for i in range(l1):
        	f.append([-1 for j in range(l2)])

        if word1[0] == word2[0]: f[0][0] = 0
        else: f[0][0] = 1

        def dp(i,j):
            if i<0 or j<0: return 0xfffffff
            if f[i][j] >= 0: return f[i][j]
            ret = 0xfffffff
            ret = min(ret,dp(i-1,j)+1)
            g = 0 if word1[i]==word2[j] else 1
            ret = min(ret,dp(i-1,j-1)+g)
            ret = min(ret,dp(i,j-1)+1)
            f[i][j] = ret
            return f[i][j]
            
        dp(l1-1,l2-1)
        return f[l1-1][l2-1]

if __name__ == '__main__':
	s = Solution()
	print s.minDistance('acca','abc')
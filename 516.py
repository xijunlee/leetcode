#!/usr/bin/env python
# coding=utf-8
import pdb

class Solution(object):
    ans = 0
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        f = [[-1 for i in xrange(len(s))] for j in xrange(len(s))]
        for i in xrange(len(s)): f[i][i] = 1
        for i in xrange(len(s)-1):
            if s[i]==s[i+1]:
                f[i][i+1] = 2
            else: f[i][i+1] = 1

        def dp(i,j):
            #pdb.set_trace()
            if i > j: return 0
            if f[i][j] >= 0: return f[i][j]
                
            if s[i] == s[j]:
                f[i][j] = max(dp(i+1,j),dp(i,j-1),dp(i+1,j-1)+2)
            else:
                f[i][j] = max(dp(i+1,j),dp(i,j-1),dp(i+1,j-1))

            return f[i][j]

        dp(0,len(s)-1)
        return f[0][len(s)-1]

if __name__ == '__main__':
    s = Solution()
    print s.longestPalindromeSubseq("bbbab")



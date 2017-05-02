#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def helper(ans,l,open,close,max):
            if len(l) == 2*n:
                ans.append(l)
                return
            if open<max:
                helper(ans,l+'(',open+1,close,max)
            if close < open:
                helper(ans,l+')',open,close+1,max)
            return 

        helper(ans,'',0,0,n)
        return ans



#!/usr/bin/env python
# coding=utf-8
import pdb

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
        	return True
        if not t:
        	return False
        
        maxf = 0
        for i in range(0,len(t)):
        	if maxf >= len(s):
        		return True
        	f = maxf
        	if s[maxf] == t[i]:
        		f += 1
        	maxf = max(f, maxf)

        if maxf >= len(s):
        	return True
        return False

if __name__ == '__main__':
	s = Solution()
	print s.isSubsequence("ac", "ahbgdc")

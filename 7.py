#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if x>=0:
            ret = int(s[::-1])
        else:
            ret = int(s[0]+s[-1:-1*len(s):-1])
        if ret >= 2147483648 or ret <= -2147483647:
            ret = 0
        return ret
        

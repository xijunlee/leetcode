#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f1, f2 = 1, 2
        for i in range(2,n):
            tmp1, tmp2 = f1, f2
            f1, f2 = tmp2, tmp1+tmp2
        if n >= 2:
            return f2
        else: 
            return f1
        
       
        
        
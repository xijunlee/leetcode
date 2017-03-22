#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ''
        if num == 0:
            ret+= '0'
            return ret
        
        l = []
        cnum = num
        if cnum < 0:
            cnum *= -1
        
        while cnum > 0:
            l.append(str(cnum % 7))
            cnum /= 7
        if num < 0:
            l.append('-')
        
        for c in reversed(l):
            ret += c
        return ret
        



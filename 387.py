#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = list(s)
        ss = set(s)
        d = {}
        for item in ss:
            d.setdefault(item,l.count(item))
        
        ret = -1
        for i in range(len(l)):
            if d[l[i]] == 1:
                ret = i
                break
        
        return ret
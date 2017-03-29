#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        sl = list(s)
        ret = ''
        for c in set(s):
            d[c]= sl.count(c)
        d = sorted(d.iteritems(), key=lambda x:x[1], reverse = True)
        for (k,v) in d:
            ret += k*v
        return ret
        
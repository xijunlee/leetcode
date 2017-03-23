#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        d = {}
        for item in set(s):
            d[item] = s.count(item)
        ret = 0
        flag = False
        for val in d.values():
            if val & 1 == 0:
                ret += val
            else:
                ret += val - 1
                flag = True
        if flag == True:
            ret += 1
        return ret
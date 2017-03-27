#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n > 0:
            if n & 1:
                ret += 1
            n = n>>1
        return ret
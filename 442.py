#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        s = set()
        for v in nums:
            if v not in s:
                s.add(v)
            else:
                ret.append(v)
        return ret
        
#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numss = list(set(nums))
        if len(numss) < 3:
            return max(numss)
        numss.remove(max(numss))
        numss.remove(max(numss))
        return max(numss)
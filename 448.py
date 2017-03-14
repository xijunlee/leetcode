#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s1 = set(nums)
        s2 = set(range(1,len(nums)+1))
        return list(s2-s1)
        



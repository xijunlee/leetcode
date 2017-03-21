#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ret = 0
        for i in range(1,len(nums)):
            ret += nums[i] - nums[0]
        return ret
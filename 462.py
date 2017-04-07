#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ret = 0
        mid = len(nums)/2
        for i in range(len(nums)):
            ret += abs(nums[i] - nums[mid])
        return ret
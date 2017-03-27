#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = -1 
        for i in range(len(nums)):
            if nums[i] >= target:
                ret = i
                break
        if nums[ret] >= target:
            return ret
    
        if ret == -1:
            return len(nums)
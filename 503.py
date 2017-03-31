#!/usr/bin/env python
# coding=utf-8


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        n = len(nums)
        nums = nums*2
        
        for i in range(0,n,1):
            k = (i+1)%n
            while k != i:
                if nums[k] > nums[i]:
                    ret.append(nums[k])
                    break
                k = (k+1)%n
            if i == len(ret):
                ret.append(-1)
        return ret
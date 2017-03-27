#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f = []
        for i in range(len(nums)):
            f.append([0 for j in range(len(nums))])
        ret = -0x7fffffff
        for i in range(0,len(nums)):
            for j in range(0,i+1):
                if i != j:
                    f[i][j] = f[i-1][j] + nums[i]
                else:
                    f[i][j] = nums[i]
                ret = max(ret, f[i][j])

        return ret
                
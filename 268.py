#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [i for i in range(len(nums)+1)]
        nums += l
        ret = 0
        for item in nums:
            ret ^= item
        return ret


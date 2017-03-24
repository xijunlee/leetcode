pyt#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for item in set(nums):
            if nums.count(item) > len(nums)/2:
                return item
        
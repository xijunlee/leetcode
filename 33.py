#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dict = {}
        for i in xrange(len(nums)):
            dict[nums[i]]=i
        if target in dict:
            return dict[target]
        else: return -1


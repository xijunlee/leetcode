#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for num in findNums:
            findPos = 0
            for i in range(len(nums)):
                if num == nums[i]:
                    findPos = i
                    break
            nextGreatNum = -1
            for i in range(findPos+1,len(nums)):
                if num < nums[i]:
                    nextGreatNum = nums[i]
                    break
            ret.append(nextGreatNum)
        return ret



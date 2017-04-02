#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for bit in range(0,32):
            countZero = 0
            countOne = 0
            for v in nums:
                if v & (1<<bit):
                    countOne +=1
                else:
                    countZero +=1
            count += countZero * countOne
        return count



#!/usr/bin/env python
# coding=utf-8
import pdb

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dict = {}
        for n in nums:
            if n not in dict:
                left, right = 0, 0
                if n-1 in dict: left = dict[n-1]
                if n+1 in dict: right = dict[n+1]
                dict[n] = left+right+1
                dict[n-left] = dict[n]
                dict[n+right] = dict[n]
        return max(dict.values())

if __name__ == '__main__':
    s = Solution()
    s.longestConsecutive([100,4,200,1,3,2])


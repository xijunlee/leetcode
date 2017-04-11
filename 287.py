#!/usr/bin/env python
# coding=utf-8
import pdb

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
                
if __name__ == '__main__':
	s = Solution()
	print s.findDuplicate([1,1,2])


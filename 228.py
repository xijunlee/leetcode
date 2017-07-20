#!/usr/bin/env python
# coding=utf-8

import pdb

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0: return []
        ret, left, right = [], 0, 0
        #pdb.set_trace()
        for i in xrange(1,len(nums)):
            if nums[i]-nums[i-1] > 1:
                if left == right: ret.append(str(nums[left]))
                else: ret.append(str(nums[left])+'->'+str(nums[right]))
                left, right = i, i
            else:
                right = i
        if left == right: ret.append(str(nums[left]))
        else: ret.append(str(nums[left])+'->'+str(nums[right]))
        return ret

if __name__ == '__main__':
    s = Solution()
    print s.summaryRanges([1])



            
        


#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        snums = sorted(nums,reverse = True)
        rank = ['Gold Medal','Silver Medal','Bronze Medal'] + map(str,range(4,len(nums)+1))
        d = dict(zip(snums,rank))
        ret = map(d.get,nums)
        return ret
            
                


#!/usr/bin/env python
# coding=utf-8

#trivial solution
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        f = [0 for i in xrange(len(nums))]
        for i in xrange(1,len(nums)+1):
        	f[i] = f[i-1]+nums[i-1]
        for i in xrange(0,len(nums)+1):
        	for j in xrange(i+1,len(nums)+1):
        		if f[j]-f[i] == k: count += 1
        return count

#map solution
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count, ans, cur = {0:1}, 0, 0
        for v in nums:
            cur += v
            ans += count.get(cur-k,0)
            count[cur] = count.get(cur,0)+1
        return ans
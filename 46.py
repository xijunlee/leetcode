#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d, ans, l = {}, [], len(nums)
        for i in xrange(l):
            d[i] = 0
        
        def dfs(step, lis):
            if step >= l:
                ans.append(lis)
                return
            for i in xrange(l):
                if not d[i]:
                    d[i] = 1
                    dfs(step+1,lis+[nums[i]])
                    d[i] = 0
            return

        dfs(0,[])
        return ans


#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ret = []
        
        def dfs(step, index, target, path):
        	if step > k or target < 0:
        		return
        	if target == 0 and step == k:
        		ret.append(path)
        	for i in range(index+1,10):
        		dfs(step+1,i,target-i,path+[i])

        dfs(0,0,n,[])

        return ret
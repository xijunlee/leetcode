#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        numss = []
        for v in nums:
        	if v: numss.append(v)
        l = len(numss)
        mask = sum(numss)
        count = 0
        for v in range(2**l):
        	tmp = mask
        	i = 0
        	while v:
        		if v & 1: tmp -= 2*numss[i]
        		v >>= 1
        		i += 1
        	if tmp == S:
        		count += 1
        return count

if __name__ == '__main__':
	s = Solution()
	print s.findTargetSumWays([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],1)


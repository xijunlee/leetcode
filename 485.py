#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = [0]
        s2 = [0]
        s3 = s1+nums+s2
        zeroPos = []
        for i in range(len(s3)):
            if s3[i] == 0:
                zeroPos.append(i)
        
        lenArr = []
        for i in range(1,len(zeroPos)):
            lenArr.append(zeroPos[i]-zeroPos[i-1]-1)
        return max(lenArr)


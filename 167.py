#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)/2+1):
            searchNum = target - numbers[i]
            st = i+1
            ed = len(numbers)-1
            mid = -1
            while st < ed:
                mid = (st+ed)/2
                if numbers[mid] == searchNum:
                    break
                if numbers[mid] > searchNum:
                    ed = mid-1
                else:
                    st = mid+1
            if numbers[(st+ed)/2] == searchNum:
                return [i+1,(st+ed)/2+1]


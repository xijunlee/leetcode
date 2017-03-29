#!/usr/bin/env python
# coding=utf-8

'''
学到了：
1、range函数中要注意第一个参数是起始位，是包括的，而第二个参数是终止位，不包括在内的，第三个参数是步进值
2、这个想法就是一个数的前面所有的数乘起来，后面的数乘起来
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        output = []
        p = 1
        n = len(nums)
        for i in range(0,n):
            output.append(p)
            p *= nums[i]
        
        p = 1
        for i in range(n-1,-1,-1):
            output[i] *= p
            p*= nums[i]
        
        return output

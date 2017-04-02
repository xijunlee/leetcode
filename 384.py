#!/usr/bin/env python
# coding=utf-8

'''
学到了：
1、如何使用python中的lambda表达式: lambda 参数：操作(参数)，lambda表达式就是一个函数而已，
多用于短的函数。lambda同样可以不带参数，就如此题中的那样
2、random.sample([list],length of samples)

'''

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.reset = lambda : nums
        self.shuffle = lambda : random.sample(nums,len(nums))

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


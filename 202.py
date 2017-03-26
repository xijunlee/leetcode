#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = False 
        k = 0
        while flag == False and k<100:
            tmp = n
            count = 0
            while tmp:
                count += (tmp % 10) ** 2
                tmp /= 10
            if count == 1:
                flag = True
            n = count
            k += 1
        return flag
        


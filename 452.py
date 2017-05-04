#!/usr/bin/env python
# coding=utf-8

'''
1、python list的按某个值排序，利用lambda表达式
2、-float('inf')
'''

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key = lambda x: x[1])
        ans, end = 0, -float('inf')
        for p in points:
            if p[0] > end:
                ans += 1
                end = p[1]
        return ans


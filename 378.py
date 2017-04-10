#!/usr/bin/env python
# coding=utf-8

'''
该题本身没什么难度，但能学到如何使用python中的heapq模块来快速进行堆排序
'''

from heapq import heappush, heappop, heapreplace, heapify
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        h = [(row[0], row, 1) for row in matrix]
        heapify(h)

        # Since we want to find kth, we pop the first k elements 
        for _ in xrange(k - 1):
            v, r, i = h[0]
            if i < len(r):
                heapreplace(h, (r[i], r, i + 1))
            else:
                heappop(h)

        return h[0][0]
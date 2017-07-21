#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        left, l = n, len(flowerbed)
        for i in xrange(l):
            if left == 0: break
            if flowerbed[i] == 0:
                f1, f2 = True, True
                if i-1>=0 and flowerbed[i-1]==1: f1 = False
                if i+1<l and flowerbed[i+1]==1: f2 = False
                if f1 and f2:
                    flowerbed[i] = 1
                    left -= 1
        return True if left == 0 else False


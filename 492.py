#!/usr/bin/env python
# coding=utf-8

import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        mid = int(math.sqrt(area))
        while mid > 0:
            if area % mid == 0:
                return [area/mid,mid]
            mid -= 1


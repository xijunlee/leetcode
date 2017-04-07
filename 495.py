#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        st, ed, s = timeSeries[0], timeSeries[0]+duration, 0
        for i in range(1,len(timeSeries)):
            if ed < timeSeries[i]: 
                s += ed-st
                st, ed = timeSeries[i], timeSeries[i]+duration
            else: ed = max(ed,timeSeries[i]+duration)
        return s + ed - st
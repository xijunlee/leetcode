#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ret = []
        d = {}
        for v in nums:
            if d.has_key(v):
                d[v] += 1
            else:
                d[v] = 1
        d = sorted(d.iteritems(), key=lambda x:x[1], reverse = True)
        for i in range(0,k):
            ret.append(d[i][0])
        return ret
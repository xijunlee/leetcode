#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret = 0 
        last = 0
        i = 0
        prices.append(0)
        while i<len(prices)-1:
            if prices[i+1] < prices[i]:
                ret += prices[i] - prices[last]
                last = i+1
            i += 1
        return ret
                
            
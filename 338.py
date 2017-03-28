#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0]
        for v in range(1,num+1):
            if v % 4 == 0: ret.append(ret[v>>1])
            else:
                ret.append(ret[v-1]+v%2)
        return ret[0:num+1]
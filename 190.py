#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a = [0 for i in range(32)]
        mask = 1
        i = 0
        #pdb.set_trace()
        while n:
            if n & mask: a[i] = 1
            n = n >> 1
            i += 1
        ret = 0
        i = 0
        for i in range(32):
        	if a[i]: ret += 1 << (31-i)
        return ret
        

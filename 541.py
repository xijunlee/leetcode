#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s1, s2 = list(s), []
        l = len(s)
        for i in range(0,l,2*k):
            if l-i >= 2*k:
                for j in range(i+k-1,i-1,-1):
                    s2.append(s1[j])
                for j in range(i+k,i+2*k,1):
                    s2.append(s1[j])
            elif l-i<2*k and l-i>=k:
                for j in range(i+k-1,i-1,-1):
                    s2.append(s1[j])
                for j in range(i+k,l,1):
                    s2.append(s1[j])
            elif l-i < k:
                for j in range(l-1,i-1,-1):
                    s2.append(s1[j])
        return ''.join(s2)


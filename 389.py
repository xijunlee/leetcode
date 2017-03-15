#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sCount = 0
        tCount = 0
        for item in s:
            sCount += ord(item)
        for item in t:
            tCount += ord(item)
        return chr(tCount - sCount)


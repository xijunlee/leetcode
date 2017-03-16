#!/usr/bin/env python
# coding=utf-8


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num % 9 == 0:
            if num > 0:
                return 9
            else:
                return 0
        else:
            return num % 
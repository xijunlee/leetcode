#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        d['A'] = s.count('A')
        d['L'] = False
        if s.find('LLL') >= 0: d['L'] = True
        if d['A'] > 1 or d['L']: return False
        else: return True

if __name__ == '__main__':
    s = Solution()
    print s.checkRecord("PPALLP")


#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        b = [1 for i in xrange(n+1)]
        b[0] = 0
        for k in xrange(2,n+1):
            i = k
            while i <= n:
                b[i] = (b[i]+1)%2
                i += k
        return sum(b)

if __name__ == '__main__':
    s = Solution()
    for i in xrange(100):
        print i, s.bulbSwitch(i)



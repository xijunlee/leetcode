#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a = (not (num&(num-1)))
        b = (num&0x55555555)
        print a,b
        if (a and b):
        	return True
        else:
        	return False

if __name__ == '__main__':
	s = Solution()
	print s.isPowerOfFour(5)

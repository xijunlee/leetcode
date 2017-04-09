#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, i = [1,2,2], 2
        while len(a) < n:
        	if a[i] == 1 and a[-1] == 1: a += [2]
        	elif a[i] == 1 and a[-1] == 2: a += [1]
        	elif a[i] == 2 and a[-1] == 1: a += [2,2]
        	elif a[i] == 2 and a[-1] == 2: a += [1,1]
        	i += 1
        return a[:n].count(1)

if __name__ == '__main__':
	s = Solution()
	print s.magicalString(6)

        

